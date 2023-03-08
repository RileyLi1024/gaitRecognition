
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import imageio
import logging
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.interpolate import UnivariateSpline
import tensorflow as tf
import sys
import re

sys.path.append("./src")
import data_utils
import viz
import cameras
import linear_model

# from openpose_3dpose_sandbox import read_openpose_json, show_anim_curves

order = [15, 12, 25, 26, 27, 17, 18, 19, 1, 2, 3, 6, 7, 8]
modelPath = "./model"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tf.app.flags.DEFINE_float("learning_rate", 1e-3, "Learning rate")
tf.app.flags.DEFINE_float("dropout", 1, "Dropout keep probability. 1 means no dropout")
tf.app.flags.DEFINE_integer("batch_size", 64, "Batch size to use during training")
tf.app.flags.DEFINE_integer("epochs", 200, "How many epochs we should train for")
tf.app.flags.DEFINE_boolean("camera_frame", False, "Convert 3d poses to camera coordinates")
tf.app.flags.DEFINE_boolean("max_norm", False, "Apply maxnorm constraint to the weights")
tf.app.flags.DEFINE_boolean("batch_norm", False, "Use batch_normalization")

# Data loading
tf.app.flags.DEFINE_boolean("predict_14", False, "predict 14 joints")
tf.app.flags.DEFINE_boolean("use_sh", False, "Use 2d pose predictions from StackedHourglass")
tf.app.flags.DEFINE_string("action","All", "The action to train on. 'All' means all the actions")

# Architecture
tf.app.flags.DEFINE_integer("linear_size", 1024, "Size of each model layer.")
tf.app.flags.DEFINE_integer("num_layers", 2, "Number of layers in the model.")
tf.app.flags.DEFINE_boolean("residual", False, "Whether to add a residual connection every 2 layers")

# Evaluation
tf.app.flags.DEFINE_boolean("procrustes", False, "Apply procrustes analysis at test time")
tf.app.flags.DEFINE_boolean("evaluateActionWise",False, "The dataset to use either h36m or heva")

# Directories
tf.app.flags.DEFINE_string("cameras_path","data/h36m/cameras.h5","Directory to load camera parameters")
tf.app.flags.DEFINE_string("data_dir",   "data/h36m/", "Data directory")
tf.app.flags.DEFINE_string("train_dir", "experiments", "Training directory.")

# openpose
tf.app.flags.DEFINE_string("pose_estimation_json", "./tmp/", "pose estimation json output directory, openpose or tf-pose-estimation")
tf.app.flags.DEFINE_boolean("interpolation", False, "interpolate openpose json")
tf.app.flags.DEFINE_float("multiplier", 0.1, "interpolation frame range")
tf.app.flags.DEFINE_boolean("write_gif", False, "write final anim gif")
tf.app.flags.DEFINE_integer("gif_fps", 30, "output gif framerate")
tf.app.flags.DEFINE_integer("verbose", 0, "0:Error, 1:Warning, 2:INFO*(default), 3:debug")
tf.app.flags.DEFINE_boolean("cache_on_fail", True, "caching last valid frame on invalid frame")

# Train or load
tf.app.flags.DEFINE_boolean("sample", False, "Set to True for sampling.")
tf.app.flags.DEFINE_boolean("use_cpu", False, "Whether to use the CPU")
# tf.app.flags.DEFINE_integer("load", 0, "Try to load a previous checkpoint.")
tf.app.flags.DEFINE_integer("load", 1, "Try to load a previous checkpoint.")

tf.app.flags.DEFINE_boolean("use_fp16", False, "Train using fp16 instead of fp32.")

FLAGS = tf.app.flags.FLAGS
train_dir = os.path.join( FLAGS.train_dir,
  FLAGS.action,
  'dropout_{0}'.format(FLAGS.dropout),
  'epochs_{0}'.format(FLAGS.epochs) if FLAGS.epochs > 0 else '',
  'lr_{0}'.format(FLAGS.learning_rate),
  'residual' if FLAGS.residual else 'not_residual',
  'depth_{0}'.format(FLAGS.num_layers),
  'linear_size{0}'.format(FLAGS.linear_size),
  'batch_size_{0}'.format(FLAGS.batch_size),
  'procrustes' if FLAGS.procrustes else 'no_procrustes',
  'maxnorm' if FLAGS.max_norm else 'no_maxnorm',
  'batch_normalization' if FLAGS.batch_norm else 'no_batch_normalization',
  'use_stacked_hourglass' if FLAGS.use_sh else 'not_stacked_hourglass',
  'predict_14' if FLAGS.predict_14 else 'predict_17')
summaries_dir = os.path.join( train_dir, "log" ) # Directory for TB summaries

def create_model( session, actions, batch_size ):
  """
  Create model and initialize it or load its parameters in a session

  Args
    session: tensorflow session
    actions: list of string. Actions to train/test on
    batch_size: integer. Number of examples in each batch
  Returns
    model: The created (or loaded) model
  Raises
    ValueError if asked to load a model, but the checkpoint specified by
    FLAGS.load cannot be found.
  """

  model = linear_model.LinearModel(FLAGS.linear_size, FLAGS.num_layers,
      FLAGS.residual, FLAGS.batch_norm, FLAGS.max_norm,
      batch_size, FLAGS.learning_rate, summaries_dir,
      FLAGS.predict_14, dtype=tf.float16 if FLAGS.use_fp16 else tf.float32)

  # Load a previously saved model
  global modelPath
  ckpt = tf.train.get_checkpoint_state( modelPath, latest_filename="checkpoint")
  print( "train_dir", train_dir )
  ckpt_name = os.path.join(os.path.join(modelPath, "checkpoint-{0}".format(FLAGS.load)))

  if len(ckpt_name) is not 0:
    print("Loading model {0}".format( ckpt_name ))
    model.saver.restore( session, ckpt.model_checkpoint_path )
    return model
  else:
    print("Could not find checkpoint. Aborting.")
    raise( ValueError, "Checkpoint {0} does not seem to exist".format( ckpt.model_checkpoint_path ) )

  return model


def read_openpose_json(openpose_output_dir, smooth=True, *args):
    # openpose output format:
    # [x1,y1,c1,x2,y2,c2,...]
    # ignore confidence score, take x and y [x1,y1,x2,y2,...]

    logger.info("start reading json files")
    # load json files
    json_files = os.listdir(openpose_output_dir)
    # check for other file types
    json_files = sorted([filename for filename in json_files if filename.endswith(".json")])
    cache = {}
    smoothed = {}
    ### extract x,y and ignore confidence score
    for file_name in json_files:
        logger.debug("reading {0}".format(file_name))
        _file = os.path.join(openpose_output_dir, file_name)
        if not os.path.isfile(_file): raise Exception("No file found!!, {0}".format(_file))
        data = json.load(open(_file))
        # take first person
        _data = data["people"][0]["pose_keypoints_2d"] if "pose_keypoints_2d" in data["people"][0] else \
        data["people"][0]["pose_keypoints"]
        xy = []
        if len(_data) >= 53:
            # openpose incl. confidence score
            # ignore confidence score
            for o in range(0, len(_data), 3):
                xy.append(_data[o])
                xy.append(_data[o + 1])
        else:
            # tf-pose-estimation
            xy = _data

        # get frame index from openpose 12 padding
        frame_indx = re.findall("(\d+)", file_name)
        logger.debug("found {0} for frame {1}".format(xy, str(int(frame_indx[-1]))))

        # body_25 support, convert body_25 output format to coco
        if len(_data) > 54:
            _xy = xy[0:19 * 2]
            for x in range(len(xy)):
                # del jnt 8
                if x == 8 * 2:
                    del _xy[x]
                if x == 8 * 2 + 1:
                    del _xy[x]
                # map jnt 9 to 8
                if x == 9 * 2:
                    _xy[16] = xy[x]
                    _xy[17] = xy[x + 1]
                # map jnt 10 to 9
                if x == 10 * 2:
                    _xy[18] = xy[x]
                    _xy[19] = xy[x + 1]
                    # map jnt 11 to 10
                if x == 11 * 2:
                    _xy[20] = xy[x]
                    _xy[21] = xy[x + 1]
                # map jnt 12 to 11
                if x == 12 * 2:
                    _xy[22] = xy[x]
                    _xy[23] = xy[x + 1]
                # map jnt 13 to 12
                if x == 13 * 2:
                    _xy[24] = xy[x]
                    _xy[25] = xy[x + 1]
                    # map jnt 14 to 13
                if x == 14 * 2:
                    _xy[26] = xy[x]
                    _xy[27] = xy[x + 1]
                # map jnt 15 to 14
                if x == 15 * 2:
                    _xy[28] = xy[x]
                    _xy[29] = xy[x + 1]
                # map jnt 16 to 15
                if x == 16 * 2:
                    _xy[30] = xy[x]
                    _xy[31] = xy[x + 1]
                # map jnt 17 to 16
                if x == 17 * 2:
                    _xy[32] = xy[x]
                    _xy[33] = xy[x + 1]
                # map jnt 18 to 17
                if x == 18 * 2:
                    _xy[34] = xy[x]
                    _xy[35] = xy[x + 1]
            # coco
            xy = _xy

        # add xy to frame
        cache[int(frame_indx[-1])] = xy

    plt.figure(1)
    drop_curves_plot = show_anim_curves(cache, plt)
    pngName = 'gif_output/dirty_plot.png'
    drop_curves_plot.savefig(pngName)
    logger.info('writing gif_output/dirty_plot.png')

    # exit if no smoothing
    if not smooth:
        # return frames cache incl. 18 joints (x,y)
        return cache

    if len(json_files) == 1:
        logger.info("found single json file")
        # return frames cache incl. 18 joints (x,y) on single image\json
        return cache

    if len(json_files) <= 8:
        raise Exception("need more frames, min 9 frames/json files for smoothing!!!")

    logger.info("start smoothing")

    # create frame blocks
    head_frame_block = [int(re.findall("(\d+)", o)[-1]) for o in json_files[:4]]
    tail_frame_block = [int(re.findall("(\d+)", o)[-1]) for o in json_files[-4:]]

    ### smooth by median value, n frames
    for frame, xy in cache.items():

        # create neighbor array based on frame index
        forward, back = ([] for _ in range(2))

        # joints x,y array
        _len = len(xy)  # 36

        # create array of parallel frames (-3<n>3)
        for neighbor in range(1, 4):
            # first n frames, get value of xy in postive lookahead frames(current frame + 3)
            if frame in head_frame_block:
                forward += cache[frame + neighbor]
            # last n frames, get value of xy in negative lookahead frames(current frame - 3)
            elif frame in tail_frame_block:
                back += cache[frame - neighbor]
            else:
                # between frames, get value of xy in bi-directional frames(current frame -+ 3)
                forward += cache[frame + neighbor]
                back += cache[frame - neighbor]

        # build frame range vector
        frames_joint_median = [0 for i in range(_len)]
        # more info about mapping in src/data_utils.py
        # for each 18joints*x,y  (x1,y1,x2,y2,...)~36
        for x in range(0, _len, 2):
            # set x and y
            y = x + 1
            if frame in head_frame_block:
                # get vector of n frames forward for x and y, incl. current frame
                x_v = [xy[x], forward[x], forward[x + _len], forward[x + _len * 2]]
                y_v = [xy[y], forward[y], forward[y + _len], forward[y + _len * 2]]
            elif frame in tail_frame_block:
                # get vector of n frames back for x and y, incl. current frame
                x_v = [xy[x], back[x], back[x + _len], back[x + _len * 2]]
                y_v = [xy[y], back[y], back[y + _len], back[y + _len * 2]]
            else:
                # get vector of n frames forward/back for x and y, incl. current frame
                # median value calc: find neighbor frames joint value and sorted them, use numpy median module
                # frame[x1,y1,[x2,y2],..]frame[x1,y1,[x2,y2],...], frame[x1,y1,[x2,y2],..]
                #                 ^---------------------|-------------------------^
                x_v = [xy[x], forward[x], forward[x + _len], forward[x + _len * 2],
                       back[x], back[x + _len], back[x + _len * 2]]
                y_v = [xy[y], forward[y], forward[y + _len], forward[y + _len * 2],
                       back[y], back[y + _len], back[y + _len * 2]]

            # get median of vector
            x_med = np.median(sorted(x_v))
            y_med = np.median(sorted(y_v))

            # holding frame drops for joint
            if not x_med:
                # allow fix from first frame
                if frame:
                    # get x from last frame
                    x_med = smoothed[frame - 1][x]
            # if joint is hidden y
            if not y_med:
                # allow fix from first frame
                if frame:
                    # get y from last frame
                    y_med = smoothed[frame - 1][y]

            logger.debug("old X {0} sorted neighbor {1} new X {2}".format(xy[x], sorted(x_v), x_med))
            logger.debug("old Y {0} sorted neighbor {1} new Y {2}".format(xy[y], sorted(y_v), y_med))

            # build new array of joint x and y value
            frames_joint_median[x] = x_med
            frames_joint_median[x + 1] = y_med

        smoothed[frame] = frames_joint_median

    return smoothed


def show_anim_curves(anim_dict, _plt):
    val = np.array(list(anim_dict.values()))
    for o in range(0,36,2):
        x = val[:,o]
        y = val[:,o+1]
        _plt.plot(x, 'r--', linewidth=0.2)
        _plt.plot(y, 'g', linewidth=0.2)
    return _plt


def twoDcoordsToThreeDcoords(openPoseOutputPath):
    openPoseOutputPath = "./tmp/"
    level = {0:logging.ERROR,
             1:logging.WARNING,
             2:logging.INFO,
             3:logging.DEBUG}
    logger.setLevel(level[FLAGS.verbose])

    smoothed = read_openpose_json(openPoseOutputPath)
    plt.figure(2)
    smooth_curves_plot = show_anim_curves(smoothed, plt)
    #return
    pngName = 'gif_output/smooth_plot.png'
    smooth_curves_plot.savefig(pngName)
    logger.info('writing gif_output/smooth_plot.png')

    enc_in = np.zeros((1, 64))
    enc_in[0] = [0 for i in range(64)]
    actions = data_utils.define_actions(FLAGS.action)

    SUBJECT_IDS = [1, 5, 6, 7, 8, 9, 11]
    rcams = cameras.load_cameras(FLAGS.cameras_path, SUBJECT_IDS)
    train_set_2d, test_set_2d, data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d = data_utils.read_2d_predictions(
        actions, FLAGS.data_dir)
    train_set_3d, test_set_3d, data_mean_3d, data_std_3d, dim_to_ignore_3d, dim_to_use_3d, train_root_positions, test_root_positions = data_utils.read_3d_data(
        actions, FLAGS.data_dir, FLAGS.camera_frame, rcams, FLAGS.predict_14)

    device_count = {"GPU": 1}
    png_lib = []
    before_pose = None
    with tf.Session(config=tf.ConfigProto(
            device_count=device_count,
            allow_soft_placement=True)) as sess:
        #plt.figure(3)
        batch_size = 128
        model = create_model(sess, actions, batch_size)
        iter_range = len(smoothed.keys())
        export_units = {}
        twod_export_units = {}
        for n, (frame, xy) in enumerate(smoothed.items()):
            logger.info("calc frame {0}/{1}".format(frame, iter_range))
            # map list into np array
            joints_array = np.zeros((1, 36))
            joints_array[0] = [0 for i in range(36)]
            for o in range(len(joints_array[0])):
                #feed array with xy array
                joints_array[0][o] = float(xy[o])

            twod_export_units[frame]={}
            for abs_b, __n in enumerate(range(0, len(xy),2)):
                twod_export_units[frame][abs_b] = {"translate": [xy[__n],xy[__n+1]]}

            _data = joints_array[0]
            # mapping all body parts or 3d-pose-baseline format
            for i in range(len(order)):
                for j in range(2):
                    # create encoder input
                    enc_in[0][order[i] * 2 + j] = _data[i * 2 + j]
            for j in range(2):
                # Hip
                enc_in[0][0 * 2 + j] = (enc_in[0][1 * 2 + j] + enc_in[0][6 * 2 + j]) / 2
                # Neck/Nose
                enc_in[0][14 * 2 + j] = (enc_in[0][15 * 2 + j] + enc_in[0][12 * 2 + j]) / 2
                # Thorax
                enc_in[0][13 * 2 + j] = 2 * enc_in[0][12 * 2 + j] - enc_in[0][14 * 2 + j]

            # set spine
            spine_x = enc_in[0][24]
            spine_y = enc_in[0][25]

            enc_in = enc_in[:, dim_to_use_2d]
            mu = data_mean_2d[dim_to_use_2d]
            stddev = data_std_2d[dim_to_use_2d]
            enc_in = np.divide((enc_in - mu), stddev)

            dp = 1.0
            dec_out = np.zeros((1, 48))
            dec_out[0] = [0 for i in range(48)]
            _, _, poses3d = model.step(sess, enc_in, dec_out, dp, isTraining=False)
            all_poses_3d = []
            enc_in = data_utils.unNormalizeData(enc_in, data_mean_2d, data_std_2d, dim_to_ignore_2d)
            poses3d = data_utils.unNormalizeData(poses3d, data_mean_3d, data_std_3d, dim_to_ignore_3d)
            gs1 = gridspec.GridSpec(1, 1)
            gs1.update(wspace=-0.00, hspace=0.05)  # set the spacing between axes.
            plt.axis('off')
            all_poses_3d.append( poses3d )
            enc_in, poses3d = map( np.vstack, [enc_in, all_poses_3d] )
            subplot_idx, exidx = 1, 1
            _max = 0
            _min = 10000

            for i in range(poses3d.shape[0]):
                for j in range(32):
                    tmp = poses3d[i][j * 3 + 2]
                    poses3d[i][j * 3 + 2] = poses3d[i][j * 3 + 1]
                    poses3d[i][j * 3 + 1] = tmp
                    if poses3d[i][j * 3 + 2] > _max:
                        _max = poses3d[i][j * 3 + 2]
                    if poses3d[i][j * 3 + 2] < _min:
                        _min = poses3d[i][j * 3 + 2]

            for i in range(poses3d.shape[0]):
                for j in range(32):
                    poses3d[i][j * 3 + 2] = _max - poses3d[i][j * 3 + 2] + _min
                    poses3d[i][j * 3] += (spine_x - 630)
                    poses3d[i][j * 3 + 2] += (500 - spine_y)

            # Plot 3d predictions
            ax = plt.subplot(gs1[subplot_idx - 1], projection='3d')
            ax.view_init(18, -70)

            if FLAGS.cache_on_fail:
                if np.min(poses3d) < -1000:
                    poses3d = before_pose

            p3d = poses3d
            if not poses3d is None:
                to_export = poses3d.tolist()[0]
                x,y,z = [[] for _ in range(3)]
                for o in range(0, len(to_export), 3):
                    x.append(to_export[o])
                    y.append(to_export[o+1])
                    z.append(to_export[o+2])
                export_units[frame]={}
                for jnt_index, (_x, _y, _z) in enumerate(zip(x,y,z)):
                    export_units[frame][jnt_index] = {"translate": [_x, _y, _z]}


                viz.show3Dpose(p3d, ax, lcolor="#9b59b6", rcolor="#2ecc71")

            pngName = 'png/pose_frame_{0}.png'.format(str(frame).zfill(12))
            plt.savefig(pngName)
            if FLAGS.write_gif:
                png_lib.append(imageio.imread(pngName))

            if FLAGS.cache_on_fail:
                before_pose = poses3d

    if FLAGS.write_gif:
        if FLAGS.interpolation:
            #take every frame on gif_fps * multiplier_inv
            png_lib = np.array([png_lib[png_image] for png_image in range(0,len(png_lib), int(multiplier_inv)) ])
        logger.info("creating Gif gif_output/animation.gif, please Wait!")
        imageio.mimsave('gif_output/animation.gif', png_lib, fps=FLAGS.gif_fps)

    # _out_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'maya/3d_data.json')
    # twod_out_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'maya/2d_data.json')
    # with open(_out_file, 'w') as outfile:
    #     logger.info("exported maya json to {0}".format(_out_file))
    #     json.dump(export_units, outfile)
    # with open(twod_out_file, 'w') as outfile:
    #     logger.info("exported maya json to {0}".format(twod_out_file))
    #     json.dump(twod_export_units, outfile)

    logger.info("Done!".format(pngName))


if __name__ == "__main__":
    twoDcoordsToThreeDcoords("./tmp")