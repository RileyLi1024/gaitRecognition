
"""Predicting 3d poses from 2d joints"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import random
import sys
import time
import h5py
import copy

import matplotlib.pyplot as plt
import numpy as np
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
#import tensorflow.compat.v1 as tf
#tf.disable_v2_behavior()
import procrustes
import viz
import cameras
import data_utils
import linear_model
from numpy import array

# cameraIntrinsic = (array([[ 0.92228155, -0.37726887,  0.08405321],
#        [-0.02117765, -0.26645871, -0.96361365],
#        [ 0.38593814,  0.88694304, -0.25373962]]), array([[-1637.17374541],[-3867.31734917], [ 1547.03325639]]), array([[1145.51133842],
#        [1144.77392808]]), array([[514.96819732], [501.88201854]]), array([[-0.19838409],
#        [ 0.21832368], [-0.00894781]]), array([[-0.00181336], [-0.00058721]]), '60457274')
#
# dataMean3D = np.array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, -2.55652589e-01
# , -7.11960573e+00, -9.81433058e-01, -5.65463051e+00, 3.19636009e+02
# , 7.19329269e+01, -1.01705840e+01, 6.91147892e+02, 1.55352986e+02
# , -1.15560633e+01, 7.42149725e+02, 1.66477287e+02, -1.18447102e+01
# , 7.36763064e+02, 1.65182437e+02, 2.55651315e-01, 7.11954604e+00
# , 9.81423860e-01, -5.09729780e+00, 3.27040413e+02, 7.22258095e+01
# , -9.99656606e+00, 7.08277383e+02, 1.58016408e+02, -1.12642400e+01
# , 7.48636864e+02, 1.66665977e+02, -1.14090840e+01, 7.36435064e+02
# , 1.63713810e+02, 1.21660845e-03, -8.60110629e-02, -1.93000576e-02
# , 2.90583676e+00, -2.11363307e+02, -4.74210915e+01, 5.67537804e+00
# , -4.35088906e+02, -9.76974016e+01, 5.93884964e+00, -4.91891970e+02
# , -1.10666618e+02, 7.37352083e+00, -5.83948619e+02, -1.31171400e+02
# , 5.67537804e+00, -4.35088906e+02, -9.76974016e+01, 5.41920653e+00
# , -3.83931702e+02, -8.68145417e+01, 2.95964663e+00, -1.87567488e+02
# , -4.34536934e+01, 1.26585822e+00, -1.20170579e+02, -2.82526049e+01
# , 1.26585822e+00, -1.20170579e+02, -2.82526049e+01, 1.57900698e+00
# , -1.51780249e+02, -3.52080548e+01, 8.84543993e-01, -1.07795356e+02
# , -2.56307189e+01, 8.84543993e-01, -1.07795356e+02, -2.56307189e+01
# , 5.67537804e+00, -4.35088906e+02, -9.76974016e+01, 4.67186639e+00
# , -3.83644089e+02, -8.55125784e+01, 1.67648571e+00, -1.97007177e+02
# , -4.31368363e+01, 8.70569014e-01, -1.68664569e+02, -3.73902498e+01
# , 8.70569014e-01, -1.68664569e+02, -3.73902498e+01, 1.39982512e+00
# , -2.00884252e+02, -4.47207875e+01, 5.24591115e-01, -1.65867774e+02
# , -3.68342864e+01, 5.24591115e-01, -1.65867774e+02, -3.68342864e+01])
#
# dataStd3d = np.array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.10722440e+02
# , 2.23881762e+01, 7.24629442e+01, 1.58563111e+02, 1.89338322e+02
# , 2.08804791e+02, 1.91799352e+02, 2.43200617e+02, 2.47561933e+02
# , 2.17938049e+02, 2.63285217e+02, 2.96834071e+02, 2.38588944e+02
# , 2.73101842e+02, 3.28803702e+02, 1.10721807e+02, 2.23880543e+01
# , 7.24625257e+01, 1.58804541e+02, 1.99771878e+02, 2.14706298e+02
# , 1.80019441e+02, 2.50527393e+02, 2.48532471e+02, 2.13542308e+02
# , 2.68186067e+02, 3.01932987e+02, 2.36099537e+02, 2.76896854e+02
# , 3.35285650e+02, 1.99331720e-02, 3.28409744e-02, 2.74275279e-02
# , 5.21069402e+01, 5.21140553e+01, 6.90824148e+01, 9.51536654e+01
# , 1.01330318e+02, 1.28997325e+02, 1.17424577e+02, 1.26484690e+02
# , 1.64650906e+02, 1.23602966e+02, 1.30855389e+02, 1.64333365e+02
# , 9.51536654e+01, 1.01330318e+02, 1.28997325e+02, 1.46022319e+02
# , 9.70795599e+01, 1.39527313e+02, 2.43475318e+02, 1.29822486e+02
# , 2.02301812e+02, 2.44687700e+02, 2.15018164e+02, 2.39382347e+02
# , 2.44687700e+02, 2.15018164e+02, 2.39382347e+02, 2.29596780e+02
# , 2.22589304e+02, 2.34161811e+02, 2.79422487e+02, 2.57310206e+02
# , 2.80385546e+02, 2.79422487e+02, 2.57310206e+02, 2.80385546e+02
# , 9.51536654e+01, 1.01330318e+02, 1.28997325e+02, 1.38760844e+02
# , 1.00892600e+02, 1.42441097e+02, 2.36875290e+02, 1.44912190e+02
# , 2.09808291e+02, 2.44006949e+02, 2.39750283e+02, 2.55205840e+02
# , 2.44006949e+02, 2.39750283e+02, 2.55205840e+02, 2.32859559e+02
# , 2.36910758e+02, 2.47343753e+02, 2.87219983e+02, 3.05741249e+02
# , 3.08336881e+02, 2.87219983e+02, 3.05741249e+02, 3.08336881e+02])
#
# dim_to_ignore_3d = \
#   np.array([0, 1, 2, 12, 13, 14, 15, 16, 17, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#   48, 49, 50, 60, 61, 62,63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
#   74, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95])
# dim_to_ignore_2d = np.array([8,9,10,11,18,19,20,21,22,23,28,29,32,33,40,41,42,
#                              43,44,45,46,47,48,49,56,57,58,59,60,61,62,63])

tf.app.flags.DEFINE_float("learning_rate", 1e-3, "Learning rate")
tf.app.flags.DEFINE_float("dropout", 1, "Dropout keep probability. 1 means no dropout")
tf.app.flags.DEFINE_integer("batch_size", 64, "Batch size to use during training")
tf.app.flags.DEFINE_integer("epochs", 200, "How many epochs we should train for")
tf.app.flags.DEFINE_boolean("camera_frame", False, "Convert 3d poses to camera coordinates")
tf.app.flags.DEFINE_boolean("max_norm", True, "Apply maxnorm constraint to the weights")
tf.app.flags.DEFINE_boolean("batch_norm", True, "Use batch_normalization")

# Data loading
tf.app.flags.DEFINE_boolean("predict_14", False, "predict 14 joints")
tf.app.flags.DEFINE_boolean("use_sh", True, "Use 2d pose predictions from StackedHourglass")
tf.app.flags.DEFINE_string("action","All", "The action to train on. 'All' means all the actions")

# Architecture
tf.app.flags.DEFINE_integer("linear_size", 1024, "Size of each model layer.")
tf.app.flags.DEFINE_integer("num_layers", 2, "Number of layers in the model.")
tf.app.flags.DEFINE_boolean("residual", True, "Whether to add a residual connection every 2 layers")

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
tf.app.flags.DEFINE_integer("verbose", 2, "0:Error, 1:Warning, 2:INFO*(default), 3:debug")
tf.app.flags.DEFINE_boolean("cache_on_fail", True, "caching last valid frame on invalid frame")

# Train or load
tf.app.flags.DEFINE_boolean("sample", False, "Set to True for sampling.")
tf.app.flags.DEFINE_boolean("use_cpu", False, "Whether to use the CPU")
# tf.app.flags.DEFINE_integer("load", 0, "Try to load a previous checkpoint.")
tf.app.flags.DEFINE_integer("load", 4874200, "Try to load a previous checkpoint.")

# Misc
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




print( train_dir )
summaries_dir = os.path.join( train_dir, "log" ) # Directory for TB summaries

# To avoid race conditions: https://github.com/tensorflow/tensorflow/issues/7448
# os.system('mkdir -p {}'.format(summaries_dir))
# if not os.path.exists(summaries_dir):
   # os.makedirs(summaries_dir)

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

  model = linear_model.LinearModel(
      FLAGS.linear_size,
      FLAGS.num_layers,
      FLAGS.residual,
      FLAGS.batch_norm,
      FLAGS.max_norm,
      batch_size,
      FLAGS.learning_rate,
      summaries_dir,
      FLAGS.predict_14,
      dtype=tf.float16 if FLAGS.use_fp16 else tf.float32)
  if FLAGS.load <= 0:
    # Create a new model from scratch
    print("Creating model with fresh parameters.")
    session.run( tf.global_variables_initializer() )
    return model

  # Load a previously saved model
  #ckpt = tf.train.get_checkpoint_state( train_dir, latest_filename="checkpoint")

  ckpt = tf.train.get_checkpoint_state(train_dir, latest_filename="checkpoint")

  print( "train_dir", train_dir )

  if ckpt and ckpt.model_checkpoint_path:
    # Check if the specific checkpoint exists
    if FLAGS.load > 0:
      if os.path.isfile(os.path.join(train_dir,"checkpoint-{0}.index".format(FLAGS.load))):
        ckpt_name = os.path.join( os.path.join(train_dir,"checkpoint-{0}".format(FLAGS.load)) )
      else:
        raise ValueError("Asked to load checkpoint {0}, but it does not seem to exist".format(FLAGS.load))
    else:
      ckpt_name = os.path.basename( ckpt.model_checkpoint_path )

    print("Loading model {0}".format( ckpt_name ))


    model.saver.restore( session, ckpt.model_checkpoint_path )


    return model
  else:
    print("Could not find checkpoint. Aborting.")
    raise( ValueError, "Checkpoint {0} does not seem to exist".format( ckpt.model_checkpoint_path ) )

  return model

def train():
  """Train a linear model for 3d pose estimation"""

  actions = data_utils.define_actions( FLAGS.action )

  number_of_actions = len( actions )

  # Load camera parameters
  SUBJECT_IDS = [1,5,6,7,8,9,11]
  rcams = cameras.load_cameras(FLAGS.cameras_path, SUBJECT_IDS)

  # Load 3d data and load (or create) 2d projections
  train_set_3d, test_set_3d, data_mean_3d, data_std_3d, dim_to_ignore_3d, dim_to_use_3d, train_root_positions, test_root_positions = data_utils.read_3d_data(
    actions, FLAGS.data_dir, FLAGS.camera_frame, rcams, FLAGS.predict_14 )

  # Read stacked hourglass 2D predictions if use_sh, otherwise use groundtruth 2D projections
  if FLAGS.use_sh:
    train_set_2d, test_set_2d, data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d = data_utils.read_2d_predictions(actions, FLAGS.data_dir)
  else:
    train_set_2d, test_set_2d, data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d = data_utils.create_2d_data( actions, FLAGS.data_dir, rcams )
  print( "done reading and normalizing data." )

  # Avoid using the GPU if requested
  device_count = {"GPU": 0} if FLAGS.use_cpu else {"GPU": 1}
  with tf.Session(config=tf.ConfigProto(
    device_count=device_count,
    allow_soft_placement=True )) as sess:

    # === Create the model ===
    print("Creating %d bi-layers of %d units." % (FLAGS.num_layers, FLAGS.linear_size))
    model = create_model( sess, actions, FLAGS.batch_size )
    model.train_writer.add_graph( sess.graph )
    print("Model created")

    #=== This is the training loop ===
    step_time, loss, val_loss = 0.0, 0.0, 0.0
    current_step = 0 if FLAGS.load <= 0 else FLAGS.load + 1
    previous_losses = []

    step_time, loss = 0, 0
    current_epoch = 0
    log_every_n_batches = 100

    for _ in xrange( FLAGS.epochs ):
      current_epoch = current_epoch + 1

      # === Load training batches for one epoch ===
      encoder_inputs, decoder_outputs = model.get_all_batches( train_set_2d, train_set_3d, FLAGS.camera_frame, training=True )
      nbatches = len( encoder_inputs )
      print("There are {0} train batches".format( nbatches ))
      start_time, loss = time.time(), 0.

      # === Loop through all the training batches ===
      for i in range( nbatches ):

        if (i+1) % log_every_n_batches == 0:
          # Print progress every log_every_n_batches batches
          print("Working on epoch {0}, batch {1} / {2}... ".format( current_epoch, i+1, nbatches), end="" )

        enc_in, dec_out = encoder_inputs[i], decoder_outputs[i]
        step_loss, loss_summary, lr_summary, _ =  model.step( sess, enc_in, dec_out, FLAGS.dropout, isTraining=True )

        if (i+1) % log_every_n_batches == 0:
          # Log and print progress every log_every_n_batches batches
          model.train_writer.add_summary( loss_summary, current_step )
          model.train_writer.add_summary( lr_summary, current_step )
          step_time = (time.time() - start_time)
          start_time = time.time()
          print("done in {0:.2f} ms".format( 1000*step_time / log_every_n_batches ) )

        loss += step_loss
        current_step += 1
        # === end looping through training batches ===

      loss = loss / nbatches
      print("=============================\n"
            "Global step:         %d\n"
            "Learning rate:       %.2e\n"
            "Train loss avg:      %.4f\n"
            "=============================" % (model.global_step.eval(),
            model.learning_rate.eval(), loss) )
      # === End training for an epoch ===

      # === Testing after this epoch ===
      isTraining = False

      if FLAGS.evaluateActionWise:

        print("{0:=^12} {1:=^6}".format("Action", "mm")) # line of 30 equal signs

        cum_err = 0
        for action in actions:

          print("{0:<12} ".format(action), end="")
          # Get 2d and 3d testing data for this action
          action_test_set_2d = get_action_subset( test_set_2d, action )
          action_test_set_3d = get_action_subset( test_set_3d, action )
          encoder_inputs, decoder_outputs = model.get_all_batches( action_test_set_2d, action_test_set_3d, FLAGS.camera_frame, training=False)

          act_err, _, step_time, loss = evaluate_batches( sess, model,
            data_mean_3d, data_std_3d, dim_to_use_3d, dim_to_ignore_3d,
            data_mean_2d, data_std_2d, dim_to_use_2d, dim_to_ignore_2d,
            current_step, encoder_inputs, decoder_outputs )
          cum_err = cum_err + act_err

          print("{0:>6.2f}".format(act_err))

        summaries = sess.run( model.err_mm_summary, {model.err_mm: float(cum_err/float(len(actions)))} )
        model.test_writer.add_summary( summaries, current_step )
        print("{0:<12} {1:>6.2f}".format("Average", cum_err/float(len(actions) )))
        print("{0:=^19}".format(''))

      else:

        n_joints = 17 if not(FLAGS.predict_14) else 14
        encoder_inputs, decoder_outputs = model.get_all_batches( test_set_2d, test_set_3d, FLAGS.camera_frame, training=False)

        total_err, joint_err, step_time, loss = evaluate_batches( sess, model,
          data_mean_3d, data_std_3d, dim_to_use_3d, dim_to_ignore_3d,
          data_mean_2d, data_std_2d, dim_to_use_2d, dim_to_ignore_2d,
          current_step, encoder_inputs, decoder_outputs, current_epoch )

        print("=============================\n"
              "Step-time (ms):      %.4f\n"
              "Val loss avg:        %.4f\n"
              "Val error avg (mm):  %.2f\n"
              "=============================" % ( 1000*step_time, loss, total_err ))

        for i in range(n_joints):
          # 6 spaces, right-aligned, 5 decimal places
          print("Error in joint {0:02d} (mm): {1:>5.2f}".format(i+1, joint_err[i]))
        print("=============================")

        # Log the error to tensorboard
        summaries = sess.run( model.err_mm_summary, {model.err_mm: total_err} )
        model.test_writer.add_summary( summaries, current_step )

      # Save the model
      print( "Saving the model... ", end="" )
      start_time = time.time()
      print("current working directory; " + os.getcwd())
      print("model saving path: " + os.path.join(train_dir, 'checkpoint'))
      #The path exceeds the limit of win10(256)
      #Enable Win32 long path in local policy editor
      #在运行中输入gpedit.msc 进入本地组策略编辑器>计算机配置>管理模板>系统>文件系统
      model.saver.save(sess, os.path.join(train_dir, 'checkpoint'), global_step=current_step )
      # model.saver.save(sess, "experiments\\All\\checkpoint", global_step=current_step )
      print( "done in {0:.2f} ms".format(1000*(time.time() - start_time)) )

      # Reset global time and loss
      step_time, loss = 0, 0

      sys.stdout.flush()


def get_action_subset( poses_set, action ):
  """
  Given a preloaded dictionary of poses, load the subset of a particular action

  Args
    poses_set: dictionary with keys k=(subject, action, seqname),
      values v=(nxd matrix of poses)
    action: string. The action that we want to filter out
  Returns
    poses_subset: dictionary with same structure as poses_set, but only with the
      specified action.
  """
  return {k:v for k, v in poses_set.items() if k[1] == action}


def evaluate_batches( sess, model,
  data_mean_3d, data_std_3d, dim_to_use_3d, dim_to_ignore_3d,
  data_mean_2d, data_std_2d, dim_to_use_2d, dim_to_ignore_2d,
  current_step, encoder_inputs, decoder_outputs, current_epoch=0 ):
  """
  Generic method that evaluates performance of a list of batches.
  May be used to evaluate all actions or a single action.

  Args
    sess
    model
    data_mean_3d
    data_std_3d
    dim_to_use_3d
    dim_to_ignore_3d
    data_mean_2d
    data_std_2d
    dim_to_use_2d
    dim_to_ignore_2d
    current_step
    encoder_inputs
    decoder_outputs
    current_epoch
  Returns

    total_err
    joint_err
    step_time
    loss
  """

  n_joints = 17 if not(FLAGS.predict_14) else 14
  nbatches = len( encoder_inputs )

  # Loop through test examples
  all_dists, start_time, loss = [], time.time(), 0.
  log_every_n_batches = 100
  for i in range(nbatches):

    if current_epoch > 0 and (i+1) % log_every_n_batches == 0:
      print("Working on test epoch {0}, batch {1} / {2}".format( current_epoch, i+1, nbatches) )

    enc_in, dec_out = encoder_inputs[i], decoder_outputs[i]
    dp = 1.0 # dropout keep probability is always 1 at test time
    step_loss, loss_summary, poses3d = model.step( sess, enc_in, dec_out, dp, isTraining=False )
    loss += step_loss

    # denormalize
    enc_in  = data_utils.unNormalizeData( enc_in,  data_mean_2d, data_std_2d, dim_to_ignore_2d )
    dec_out = data_utils.unNormalizeData( dec_out, data_mean_3d, data_std_3d, dim_to_ignore_3d )
    poses3d = data_utils.unNormalizeData( poses3d, data_mean_3d, data_std_3d, dim_to_ignore_3d )

    # Keep only the relevant dimensions
    dtu3d = np.hstack( (np.arange(3), dim_to_use_3d) ) if not(FLAGS.predict_14) else  dim_to_use_3d

    dec_out = dec_out[:, dtu3d]
    poses3d = poses3d[:, dtu3d]

    assert dec_out.shape[0] == FLAGS.batch_size
    assert poses3d.shape[0] == FLAGS.batch_size

    if FLAGS.procrustes:
      # Apply per-frame procrustes alignment if asked to do so
      for j in range(FLAGS.batch_size):
        gt  = np.reshape(dec_out[j,:],[-1,3])
        out = np.reshape(poses3d[j,:],[-1,3])
        _, Z, T, b, c = procrustes.compute_similarity_transform(gt,out,compute_optimal_scale=True)
        out = (b*out.dot(T))+c

        poses3d[j,:] = np.reshape(out,[-1,17*3] ) if not(FLAGS.predict_14) else np.reshape(out,[-1,14*3] )

    # Compute Euclidean distance error per joint
    sqerr = (poses3d - dec_out)**2 # Squared error between prediction and expected output
    dists = np.zeros( (sqerr.shape[0], n_joints) ) # Array with L2 error per joint in mm
    dist_idx = 0
    for k in np.arange(0, n_joints*3, 3):
      # Sum across X,Y, and Z dimenstions to obtain L2 distance
      dists[:,dist_idx] = np.sqrt( np.sum( sqerr[:, k:k+3], axis=1 ))
      dist_idx = dist_idx + 1

    all_dists.append(dists)
    assert sqerr.shape[0] == FLAGS.batch_size

  step_time = (time.time() - start_time) / nbatches
  loss      = loss / nbatches

  all_dists = np.vstack( all_dists )

  # Error per joint and total for all passed batches
  joint_err = np.mean( all_dists, axis=0 )
  total_err = np.mean( all_dists )

  return total_err, joint_err, step_time, loss



def convert2DcoordTo3D():
  device_count = {"GPU": 0} if FLAGS.use_cpu else {"GPU": 1}
  with tf.Session(config=tf.ConfigProto(device_count=device_count)) as sess:
    print("Creating %d layers of %d units." % (FLAGS.num_layers, FLAGS.linear_size))
    batch_size = 1
    _ = []
    model = create_model(sess, _, batch_size)
    print("Model loaded")

    input = np.array([-0.57030966, -0.20899645, -0.41249613, -0.20510335, -0.3529957, 0.25010335,
                    -0.33205859, 0.41733369, -0.80935613, -0.20763942, -0.82279944, 0.28203933,
                    -0.92373614, 0.5483012, -0.56758462, -0.38710986, -0.5714109, -0.45269784,
                    -0.55365922, -0.49583955, -1.00309068, -0.37448827, -1.5036023,  -0.88227356,
                      -2.03263586, -0.93766623, -0.22516537, -0.3923183, 0.1535187, -0.83561453,
                      0.51504485, -0.7036885])
    input = np.array([0.54, 0.82, 0.49, 0.60, 0.51, 0.47, 0.63, 0.46, 0.69, 0.62, 0.72, 0.79,
                      0.57, 0.46, 0.55, 0.34, 0.53, 0.22, 0.52, 0.16, 0.32, 0.31, 0.38, 0.27,
                      0.44, 0.22, 0.61, 0.22, 0.67, 0.34, 0.68, 0.46])
    input = input.reshape([1, 32])
    # [-0.57962293 - 0.24144559 - 0.41249613 - 0.23740726 - 0.3529957   0.19037466
    #  - 0.27318489  0.49006088 - 0.81907327 - 0.24024535 - 0.82279944  0.21948831
    #  - 0.92373614  0.49233781 - 0.57662929 - 0.31853846 - 0.58043251 - 0.40013485
    #  - 0.56234866 - 0.44760577 - 0.93645115 - 0.40194545 - 1.43776073 - 0.90958877
    #  - 2.04188761 - 0.96191016 - 0.17690191 - 0.32414467  0.1535187 - 0.77014473
    #  0.51504485 - 0.72620372]

    threeDcoords = model.predict3DcoordForABatch(sess, input)
    poses3d = data_utils.unNormalizeData( threeDcoords[0], dataMean3D, dataStd3d, dim_to_ignore_3d )
    R, T, f, c, k, p, name = cameraIntrinsic
    def cam2world_centered(data_3d_camframe):
      N_JOINTS_H36M = 32
      data_3d_worldframe = cameras.camera_to_world_frame(data_3d_camframe.reshape((-1, 3)), R, T)
      data_3d_worldframe = data_3d_worldframe.reshape((-1, N_JOINTS_H36M * 3))
      # subtract root translation
      return data_3d_worldframe - np.tile(data_3d_worldframe[:, :3], (1, N_JOINTS_H36M))

    poses3d = cam2world_centered(poses3d)
    inputWithIgnore = np.array([473.00000196,413.00000032,486.00000166,412.99999966,493.00000112
                      ,510.00000016,492.99999836,592.00000034,0.,0.
                      ,0.,0.,451.99999737,413.00000026,444.99999994
                      ,510.00000071,430.99999811,599.00000119,0.,0.
                      ,0.,0.,0.,0.,472.9999981
                      ,303.00000085,473.0000001,283.00000006,0.,0.
                      ,473.00000202,228.00000092,0.,0.,430.99999425
                      ,303.00000074,376.00000363,310.00000056,314.99999276,309.99999907
                      ,0.,0.,0.,0.,0.
                      ,0.,0.,0.,0.,0.
                      ,507.00000078,302.99999954,555.00000095,310.0000022,603.00000262
                      ,316.99999955,0.,0.,0.,0.
                      ,0.,0.,0.,0.,])
    inputWithIgnore = inputWithIgnore.reshape([1, 64])

    import matplotlib.gridspec as gridspec
    # 1080p	= 1,920 x 1,080
    fig = plt.figure(figsize=(19.2, 10.8))

    gs1 = gridspec.GridSpec(1, 2)  # 5 rows, 9 columns
    gs1.update(wspace=-0.00, hspace=0.05)  # set the spacing between axes.
    plt.axis('off')
    subplot_idx, exidx = 1, 1

    # # Plot 2d pose
    ax1 = plt.subplot(gs1[0])
    viz.show2Dpose(inputWithIgnore, ax1)
    ax1.invert_yaxis()

    # Plot 3d predictions
    ax3 = plt.subplot(gs1[1], projection='3d')
    # p3d = poses3d[exidx, :]
    viz.show3Dpose(poses3d, ax3, lcolor="#9b59b6", rcolor="#2ecc71")

    plt.show()
    a = 0





def sample():
  """Get samples from a model and visualize them"""

  actions = data_utils.define_actions( FLAGS.action )

  # Load camera parameters
  SUBJECT_IDS = [1,5,6,7,8,9,11]
  rcams = cameras.load_cameras(FLAGS.cameras_path, SUBJECT_IDS)

  # Load 3d data and load (or create) 2d projections
  train_set_3d, test_set_3d, data_mean_3d, data_std_3d, dim_to_ignore_3d, dim_to_use_3d, train_root_positions, test_root_positions = data_utils.read_3d_data(
    actions, FLAGS.data_dir, FLAGS.camera_frame, rcams, FLAGS.predict_14 )

  if FLAGS.use_sh:
    train_set_2d, test_set_2d, data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d = data_utils.read_2d_predictions(actions, FLAGS.data_dir)
  else:
    train_set_2d, test_set_2d, data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d = data_utils.create_2d_data( actions, FLAGS.data_dir, rcams )
  print( "done reading and normalizing data." )

  device_count = {"GPU": 0} if FLAGS.use_cpu else {"GPU": 1}
  with tf.Session(config=tf.ConfigProto( device_count = device_count )) as sess:
    # === Create the model ===
    print("Creating %d layers of %d units." % (FLAGS.num_layers, FLAGS.linear_size))
    batch_size = 128
    model = create_model(sess, actions, batch_size)
    print("Model loaded")

    for key2d in test_set_2d.keys():

      (subj, b, fname) = key2d
      print( "Subject: {}, action: {}, fname: {}".format(subj, b, fname) )

      # keys should be the same if 3d is in camera coordinates
      key3d = key2d if FLAGS.camera_frame else (subj, b, '{0}.h5'.format(fname.split('.')[0]))
      key3d = (subj, b, fname[:-3]) if (fname.endswith('-sh')) and FLAGS.camera_frame else key3d

      enc_in  = test_set_2d[ key2d ]
      n2d, _ = enc_in.shape
      dec_out = test_set_3d[ key3d ]
      n3d, _ = dec_out.shape
      assert n2d == n3d

      # Split into about-same-size batches
      enc_in   = np.array_split( enc_in,  n2d // batch_size )
      dec_out  = np.array_split( dec_out, n3d // batch_size )
      all_poses_3d = []

      for bidx in range( len(enc_in) ):

        # Dropout probability 0 (keep probability 1) for sampling
        dp = 1.0
        _, _, poses3d = model.step(sess, enc_in[bidx], dec_out[bidx], dp, isTraining=False)
        # _, _, poses3d = model.step(sess, enc_in[bidx], _, dp, isTraining=False)

        # denormalize
        enc_in[bidx]  = data_utils.unNormalizeData(  enc_in[bidx], data_mean_2d, data_std_2d, dim_to_ignore_2d )
        dec_out[bidx] = data_utils.unNormalizeData( dec_out[bidx], data_mean_3d, data_std_3d, dim_to_ignore_3d )
        poses3d = data_utils.unNormalizeData( poses3d, data_mean_3d, data_std_3d, dim_to_ignore_3d )
        all_poses_3d.append( poses3d )

      # Put all the poses together
      enc_in, dec_out, poses3d = map( np.vstack, [enc_in, dec_out, all_poses_3d] )

      # Convert back to world coordinates
      if FLAGS.camera_frame:
        N_CAMERAS = 4
        N_JOINTS_H36M = 32

        # Add global position back
        dec_out = dec_out + np.tile( test_root_positions[ key3d ], [1,N_JOINTS_H36M] )

        # Load the appropriate camera
        subj, _, sname = key3d

        cname = sname.split('.')[1] # <-- camera name
        scams = {(subj,c+1): rcams[(subj,c+1)] for c in range(N_CAMERAS)} # cams of this subject
        scam_idx = [scams[(subj,c+1)][-1] for c in range(N_CAMERAS)].index( cname ) # index of camera used
        the_cam  = scams[(subj, scam_idx+1)] # <-- the camera used
        R, T, f, c, k, p, name = the_cam
        assert name == cname

        def cam2world_centered(data_3d_camframe):
          data_3d_worldframe = cameras.camera_to_world_frame(data_3d_camframe.reshape((-1, 3)), R, T)
          data_3d_worldframe = data_3d_worldframe.reshape((-1, N_JOINTS_H36M*3))
          # subtract root translation
          return data_3d_worldframe - np.tile( data_3d_worldframe[:,:3], (1,N_JOINTS_H36M) )

        # Apply inverse rotation and translation
        dec_out = cam2world_centered(dec_out)
        poses3d = cam2world_centered(poses3d)

  # Grab a random batch to visualize
  enc_in, dec_out, poses3d = map( np.vstack, [enc_in, dec_out, poses3d] )
  idx = np.random.permutation( enc_in.shape[0] )
  enc_in, dec_out, poses3d = enc_in[idx, :], dec_out[idx, :], poses3d[idx, :]

  # Visualize random samples
  import matplotlib.gridspec as gridspec

  # 1080p	= 1,920 x 1,080
  fig = plt.figure( figsize=(19.2, 10.8) )

  gs1 = gridspec.GridSpec(5, 9) # 5 rows, 9 columns
  gs1.update(wspace=-0.00, hspace=0.05) # set the spacing between axes.
  plt.axis('off')

  subplot_idx, exidx = 1, 1
  nsamples = 15
  for i in np.arange( nsamples ):

    # Plot 2d pose
    ax1 = plt.subplot(gs1[subplot_idx-1])
    p2d = enc_in[exidx,:]
    viz.show2Dpose( p2d, ax1 )
    ax1.invert_yaxis()

    # Plot 3d gt
    ax2 = plt.subplot(gs1[subplot_idx], projection='3d')
    p3d = dec_out[exidx,:]
    viz.show3Dpose( p3d, ax2 )

    # Plot 3d predictions
    ax3 = plt.subplot(gs1[subplot_idx+1], projection='3d')
    p3d = poses3d[exidx,:]
    viz.show3Dpose( p3d, ax3, lcolor="#9b59b6", rcolor="#2ecc71" )

    exidx = exidx + 1
    subplot_idx = subplot_idx + 3

  plt.show()

def main(_):
  if FLAGS.sample:
    sample()
    convert2DcoordTo3D()
  else:
    train()

if __name__ == "__main__":
  tf.app.run()

