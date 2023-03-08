import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import tensorflow as tf
import data_utils
import viz
import re
import cameras
import json
import os
import time
from predict_3dpose import create_model
import cv2
import imageio
import logging
import scipy as sp
from pprint import pprint
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline




FLAGS = tf.app.flags.FLAGS

order = [15, 12, 25, 26, 27, 17, 18, 19, 1, 2, 3, 6, 7, 8]
data_mean_2d = np.array([534.2362067815909,425.88147731177776,533.393731182906,425.6983578158579,
                         534.3978023429365,497.43802989193154,532.481293821069,569.0466234375722,
                         0.0,0.0,0.0,0.0,535.2915655822208,425.73629461606714,532.7675617662295,
                         496.4731547066457,530.8880341233735,569.6075068344198,0.0,0.0,0.0,0.0,
                         0.0,0.0,535.7534460606558,331.2267732306162,536.3380005282891,317.4499285783894,
                         0.0,0.0,536.7162946417122,269.119694669409,0.0,0.0,536.3674026383682,
                         330.27798906492825,535.8566970903066,374.59944401417664,534.7028848175864,
                         387.35266055116455,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,534.9920256553606,
                         331.7734652688376,534.611308079746,373.81679138734876,535.2152919182024,
                         379.5077967523042,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
data_std_2d = np.array([107.37361012086936,61.634909589570334,114.89497052627252,
                        61.911997024725586,117.27565510971122,50.22711629323473,
                        118.89857526011964,55.0000570865409,0.0,0.0,0.0,0.0,
                        102.91089763326161,61.338520877316505,106.6694471505881,
                        47.96084756161423,108.13481259325421,53.60647265856601,
                        0.0,0.0,0.0,0.0,0.0,0.0,110.5622742770474,72.91669969652871,
                        110.84492972268202,76.09916642663414,0.0,0.0,115.08215260502243,
                        82.92943734420392,0.0,0.0,105.04274863959776,72.84070268738881,
                        106.31581039747435,73.21929020828857,108.0876752788032,
                        82.49487760274116,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
                        124.31763034139937,73.34214366385531,132.80917569040227,
                        76.37108859015507,131.60933137204532,88.82878858279597,0.0,0.0,
                        0.0,0.0,0.0,0.0,0.0,0.0])
dim_to_ignore_2d = np.array([8,9,10,11,18,19,20,21,22,23,28,29,32,33,40,41,42,43,
                             44,45,46,47,48,49,56,57,58,59,60,61,62,63,])
dim_to_use_2d = np.array([0,1,2,3,4,5,6,7,12,13,14,15,16,17,24,25,26,27,30,31,34,
                          35,36,37,38,39,50,51,52,53,54,55,])
data_mean_3d = np.array([0.0,0.0,0.0,-0.25565258869478036,-7.1196057274161175,-0.9814330584948379,
                         -5.654630512911174,319.63600940520956,71.93292692469369,-10.17058399414122,
                         691.147891657268,155.35298624455558,-11.556063267619042,742.1497253356404,
                         166.47728719822825,-11.844710199349015,736.7630637064799,165.18243684504364,
                         0.2556513148981798,7.119546036952684,0.9814238602344464,-5.09729779548788,
                         327.0404131275417,72.22580948277304,-9.996566061820301,708.2773832914069,
                         158.01640791345193,-11.264239970134991,748.6368635545937,166.66597679101667,
                         -11.409083950296926,736.4350641667342,163.71381003704064,0.001216608446575789,
                         -0.0860110628555832,-0.019300057626550318,2.905836755628732,-211.36330686630447,
                         -47.42109152234179,5.675378040751587,-435.08890570553115,-97.69740161233237,
                         5.938849636743831,-491.89197005409795,-110.66661784332692,7.373520833615219,
                         -583.9486185314573,-131.1714003592153,5.675378040751587,-435.08890570553115,
                         -97.69740161233237,5.419206528924146,-383.93170195731375,-86.81454166710287,
                         2.9596466251663,-187.56748832018533,-43.45369343684996,1.265858216721359,
                         -120.17057902524314,-28.25260491487501,1.265858216721359,-120.17057902524314,
                         -28.25260491487501,1.5790069800258655,-151.78024886560598,-35.208054839934334,
                         0.8845439929650551,-107.79535580945144,-25.630718856450642,0.8845439929650551,
                         -107.79535580945144,-25.630718856450642,5.675378040751587,-435.08890570553115,
                         -97.69740161233237,4.67186639021005,-383.64408934471885,-85.51257837102315,
                         1.676485712964961,-197.00717718979865,-43.136836346611275,0.870569014149015,
                         -168.66456902427169,-37.39024980077857,0.870569014149015,-168.66456902427169,
                         -37.39024980077857,1.3998251249932094,-200.88425229015638,-44.72078749985584,
                         0.524591114529577,-165.8677736676434,-36.83428638678258,0.524591114529577,
                         -165.8677736676434,-36.83428638678258,])
data_std_3d = np.array([0.0,0.0,0.0,110.72243952249467,22.388176174254344,72.46294421720371,
                        158.56311079063167,189.33832206725427,208.80479145798358,191.79935232131174,
                        243.2006168338775,247.5619329598469,217.93804873141713,263.28521663252366,
                        296.83407116431516,238.58894437069443,273.10184162210237,328.8037017541383,
                        110.72180724487369,22.388054332865146,72.46252568188348,158.80454092789694,
                        199.77187809476598,214.70629784214964,180.01944122294572,250.5273931276209,
                        248.53247137512835,213.54230838101486,268.1860672890441,301.93298650577293,
                        236.099536642125,276.89685409470394,335.2856496839525,0.019933172010044013,
                        0.0328409743677789,0.027427527942168763,52.106940182707724,52.1140552562803,
                        69.08241483855366,95.15366543888484,101.33031820020668,128.99732515433234,
                        117.42457701224566,126.48468958404064,164.6509064797144,123.60296575281787,
                        130.85538909944853,164.33336500814266,95.15366543888484,101.33031820020668,
                        128.99732515433234,146.02231892533874,97.07955985159373,139.5273125258419,
                        243.47531766057696,129.82248593326003,202.30181232857467,244.68770047899037,
                        215.01816411816674,239.3823472541272,244.68770047899037,215.01816411816674,
                        239.3823472541272,229.5967804601632,222.58930439315475,234.16181055822355,
                        279.42248695083185,257.310206217184,280.38554552569474,279.42248695083185,
                        257.310206217184,280.38554552569474,95.15366543888484,101.33031820020668,
                        128.99732515433234,138.76084446074105,100.89260001133228,142.44109658418046,
                        236.87528986742387,144.9121901303683,209.80829096235226,244.00694913404303,
                        239.75028349768985,255.20583985806604,244.00694913404303,239.75028349768985,
                        255.20583985806604,232.85955881343241,236.91075754542612,247.3437528476897,
                        287.21998293914874,305.74124862293587,308.33688068256515,287.21998293914874,
                        305.74124862293587,308.33688068256515,])
dim_to_ignore_3d = np.array([0,1,2,12,13,14,15,16,17,27,28,29,30,31,32,33,
                             34,35,48,49,50,60,61,62,63,64,65,66,67,68,69,
                             70,71,72,73,74,84,85,86,87,88,89,90,91,92,93,94,95,])
dim_to_use_3d = np.array([3,4,5,6,7,8,9,10,11,18,19,20,21,22,23,24,25,26,36,37,
                          38,39,40,41,42,43,44,45,46,47,51,52,53,54,55,56,57,58,
                          59,75,76,77,78,79,80,81,82,83,])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def show_anim_curves(anim_dict, _plt):
    val = np.array(list(anim_dict.values()))
    for o in range(0,36,2):
        x = val[:,o]
        y = val[:,o+1]
        _plt.plot(x, 'r--', linewidth=0.2)
        _plt.plot(y, 'g', linewidth=0.2)
    return _plt

def read_openpose_json(openpose_output_dir, smooth=False, *args):
    # openpose output format:
    # [x1,y1,c1,x2,y2,c2,...]
    # ignore confidence score, take x and y [x1,y1,x2,y2,...]

    logger.info("start reading json files")
    #load json files
    json_files = os.listdir(openpose_output_dir)
    # check for other file types
    json_files = sorted([filename for filename in json_files if filename.endswith(".json")])
    cache = {}
    cacheWithFilename = {}
    smoothed = {}
    ### extract x,y and ignore confidence score
    for file_name in json_files:
        logger.debug("reading {0}".format(file_name))
        _file = os.path.join(openpose_output_dir, file_name)
        if not os.path.isfile(_file): raise Exception("No file found!!, {0}".format(_file))
        data = json.load(open(_file))
        if len(data['people']) <= 0:
          continue
        #take first person
        _data = data["people"][0]["pose_keypoints_2d"] if "pose_keypoints_2d" in data["people"][0] else data["people"][0]["pose_keypoints"]
        xy = []
        if len(_data)>=53:
            #openpose incl. confidence score
            #ignore confidence score
            for o in range(0,len(_data),3):
                xy.append(_data[o])
                xy.append(_data[o+1])
        else:
            #tf-pose-estimation
            xy = _data

        # get frame index from openpose 12 padding
        frame_indx = re.findall("(\d+)", file_name)
        logger.debug("found {0} for frame {1}".format(xy, str(int(frame_indx[-1]))))

        #body_25 support, convert body_25 output format to coco
        if len(_data)>54:
            _xy = xy[0:19*2]
            for x in range(len(xy)):
                #del jnt 8
                if x==8*2:
                    del _xy[x]
                if x==8*2+1:
                    del _xy[x]
                #map jnt 9 to 8
                if x==9*2:
                    _xy[16] = xy[x]
                    _xy[17] = xy[x+1]
                #map jnt 10 to 9
                if x==10*2:
                    _xy[18] = xy[x]
                    _xy[19] = xy[x+1]         
                #map jnt 11 to 10
                if x==11*2:
                    _xy[20] = xy[x]
                    _xy[21] = xy[x+1]
                #map jnt 12 to 11
                if x==12*2:
                    _xy[22] = xy[x]
                    _xy[23] = xy[x+1]
                #map jnt 13 to 12
                if x==13*2:
                    _xy[24] = xy[x]
                    _xy[25] = xy[x+1]         
                #map jnt 14 to 13
                if x==14*2:
                    _xy[26] = xy[x]
                    _xy[27] = xy[x+1]
                #map jnt 15 to 14
                if x==15*2:
                    _xy[28] = xy[x]
                    _xy[29] = xy[x+1]
                #map jnt 16 to 15
                if x==16*2:
                    _xy[30] = xy[x]
                    _xy[31] = xy[x+1]
                #map jnt 17 to 16
                if x==17*2:
                    _xy[32] = xy[x]
                    _xy[33] = xy[x+1]
                #map jnt 18 to 17
                if x==18*2:
                    _xy[34] = xy[x]
                    _xy[35] = xy[x+1]
            #coco 
            xy = _xy

        #add xy to frame
        cache[int(frame_indx[-1])] = xy
        cacheWithFilename[file_name] = xy

    # plt.figure(1)
    # drop_curves_plot = show_anim_curves(cache, plt)
    # pngName = 'gif_output/dirty_plot.png'
    # drop_curves_plot.savefig(pngName)
    # logger.info('writing gif_output/dirty_plot.png')

    return cache, cacheWithFilename


def save3Dpose(filename, pose):

    jointName = ['Hip', 'RHip', 'RKnee', 'RFoot', 'LHip', 'LKnee', 'LFoot', 'Spine',
                 'Thorax', 'Head', 'LShoulder', 'LElbow', 'LWrist', 'RShoulder',
                 'RElbow', 'RWrist']
    jointOrder = [0, 1, 2, 3, 6, 7, 8, 12, 13, 15, 17, 18, 19, 25, 26, 27]

    global dim_to_use_3d
    with open(filename, 'w') as outFile:
        #outFile.write("PersonOrder,JointName,x,y,z\n")
        outFile.write("PersonOrder,JointName,x,y,z,\n")
        person = "person1"
        #ss = ""
        for point in range(16):
            strVal = person + "," + jointName[point] + ','
             #strVal = person + "," + jointName[point]
            for i in range(3):
                strVal = strVal + str(pose[jointOrder[point]]["translate"][i]) + ','
                #ss = ss + ',' + str(pose[jointOrder[point]]["translate"][i])
            strVal += '\n'
            #jieguo = strVal + ss + '\n'
            outFile.write(strVal)
            #outFile.write(jieguo)
    outFile.close()


def save3Dpose2(filename, pose):
    '''
    jointName = ['Hip', 'RHip', 'RKnee', 'RFoot', 'LHip',
                 'LKnee', 'LFoot', 'Spine','Thorax', 'Head',
                 'LShoulder', 'LElbow', 'LWrist', 'RShoulder','RElbow', 'RWrist']
    jointOrder = [0, 1, 2, 3, 6,
                  7, 8, 12, 13, 15,
                  17, 18, 19, 25,26, 27]
    '''
    jointName = ['LShoulder', 'RShoulder', 'Thorax', 'LHip', 'RHip', 'LElbow', 'RElbow',
                 'LWrist','RWrist', 'LKnee', 'RKnee', 'LFoot', 'RFoot', 'Head']
    jointOrder = [17, 25, 13, 6, 1, 18, 26, 19, 27, 7, 2, 8, 3, 15]

    global dim_to_use_3d
    with open(filename, 'w') as outFile:
        for point in range(14):
            strVal = str(pose[jointOrder[point]]["translate"][0]) + ',' + \
                         str(pose[jointOrder[point]]["translate"][1]) + ',' + \
                         str(pose[jointOrder[point]]["translate"][2]) + ','
            outFile.write(strVal)
    outFile.close()




def twoDcoordsToThreeDcoords(openPoseOutputPath, threeDposeOutputhPath):
    _, smoothed = read_openpose_json(openPoseOutputPath)

    print(openPoseOutputPath)


    enc_in = np.zeros((1, 64))
    enc_in[0] = [0 for i in range(64)]

    actions = data_utils.define_actions(FLAGS.action)

    SUBJECT_IDS = [1, 5, 6, 7, 8, 9, 11]
    rcams = cameras.load_cameras(FLAGS.cameras_path, SUBJECT_IDS)
    global data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d
    global data_mean_3d, data_std_3d, dim_to_ignore_3d, dim_to_use_3d

    device_count = {"GPU": 1}
    png_lib = []
    before_pose = None
    with tf.Session(config=tf.ConfigProto(
            device_count=device_count,
            allow_soft_placement=True)) as sess:
        # plt.figure(3)
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
                # feed array with xy array
                joints_array[0][o] = float(xy[o])

            twod_export_units[frame] = {}
            for abs_b, __n in enumerate(range(0, len(xy), 2)):
                twod_export_units[frame][abs_b] = {"translate": [xy[__n], xy[__n + 1]]}

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
            all_poses_3d.append(poses3d)
            enc_in, poses3d = map(np.vstack, [enc_in, all_poses_3d])
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
                x, y, z = [[] for _ in range(3)]
                for o in range(0, len(to_export), 3):
                    x.append(to_export[o])
                    y.append(to_export[o + 1])
                    z.append(to_export[o + 2])
                export_units[frame] = {}
                for jnt_index, (_x, _y, _z) in enumerate(zip(x, y, z)):
                    export_units[frame][jnt_index] = {"translate": [_x, _y, _z]}

                viz.show3Dpose(p3d, ax, lcolor="#9b59b6", rcolor="#2ecc71")

            pngName = threeDposeOutputhPath + '/{0}.png'.format(frame.split('.')[0])
            plt.savefig(pngName)

            if FLAGS.cache_on_fail:
                before_pose = poses3d

            logger.info("{0} Done!".format(pngName))

    if os.path.exists(threeDposeOutputhPath) is not True:
        os.makedirs(threeDposeOutputhPath)
    for object  in export_units.keys():
        # newIndex = "frame" + object.split('_')[0].split('e')[1].zfill(5) + "_keypoints.csv"
        
        threeDposeOutFilename = threeDposeOutputhPath + '/' + "frame" + object.split('_')[0].split('e')[1] + "_keypoints.csv"
        save3Dpose(threeDposeOutFilename, export_units[object])


def main(_):
    
    smoothed = read_openpose_json(openpose_output_dir)
    plt.figure(2)
    # smooth_curves_plot = show_anim_curves(smoothed, plt)
    # #return
    # pngName = 'gif_output/smooth_plot.png'
    # smooth_curves_plot.savefig(pngName)
    # logger.info('writing gif_output/smooth_plot.png')
    
    if FLAGS.interpolation:
        logger.info("start interpolation")

        framerange = len( smoothed.keys() )
        joint_rows = 36
        array = np.concatenate(list(smoothed.values()))
        array_reshaped = np.reshape(array, (framerange, joint_rows) )
    
        multiplier = FLAGS.multiplier
        multiplier_inv = 1/multiplier

        out_array = np.array([])
        for row in range(joint_rows):
            x = []
            for frame in range(framerange):
                x.append( array_reshaped[frame, row] )
            
            frame = range( framerange )
            frame_resampled = np.arange(0, framerange, multiplier)
            spl = UnivariateSpline(frame, x, k=3)
            #relative smooth factor based on jnt anim curve
            min_x, max_x = min(x), max(x)
            smooth_fac = max_x - min_x
            smooth_resamp = 125
            smooth_fac = smooth_fac * smooth_resamp
            spl.set_smoothing_factor( float(smooth_fac) )
            xnew = spl(frame_resampled)
            
            out_array = np.append(out_array, xnew)
    
        logger.info("done interpolating. reshaping {0} frames,  please wait!!".format(framerange))
    
        a = np.array([])
        for frame in range( int( framerange * multiplier_inv ) ):
            jnt_array = []
            for jnt in range(joint_rows):
                jnt_array.append( out_array[ jnt * int(framerange * multiplier_inv) + frame] )
            a = np.append(a, jnt_array)
        
        a = np.reshape(a, (int(framerange * multiplier_inv), joint_rows))
        out_array = a
    
        interpolate_smoothed = {}
        for frame in range( int(framerange * multiplier_inv) ):
            interpolate_smoothed[frame] = list( out_array[frame] )
        
        plt.figure(3)
        smoothed = interpolate_smoothed
        interpolate_curves_plot = show_anim_curves(smoothed, plt)
        pngName = 'gif_output/interpolate_{0}.png'.format(smooth_resamp)
        interpolate_curves_plot.savefig(pngName)
        logger.info('writing gif_output/interpolate_plot.png')

    enc_in = np.zeros((1, 64))
    enc_in[0] = [0 for i in range(64)]

    actions = data_utils.define_actions(FLAGS.action)

    SUBJECT_IDS = [1, 5, 6, 7, 8, 9, 11]
    rcams = cameras.load_cameras(FLAGS.cameras_path, SUBJECT_IDS)
    global data_mean_2d, data_std_2d, dim_to_ignore_2d, dim_to_use_2d
    global data_mean_3d, data_std_3d, dim_to_ignore_3d, dim_to_use_3d
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
        iter_range = len(smoothed[1].keys())
        export_units = {}
        twod_export_units = {}
        for n, (frame, xy) in enumerate(smoothed[1].items()):
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
            #plt.savefig(pngName)
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

    _out_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'maya/3d_data.json')
    twod_out_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'maya/2d_data.json')
    with open(_out_file, 'w') as outfile:
        logger.info("exported maya json to {0}".format(_out_file))
        json.dump(export_units, outfile)
    with open(twod_out_file, 'w') as outfile:
        logger.info("exported maya json to {0}".format(twod_out_file))
        json.dump(twod_export_units, outfile)

    logger.info("Done!".format(pngName))

if __name__ == "__main__":

    openpose_output_dir = FLAGS.pose_estimation_json
    
    level = {0:logging.ERROR,
             1:logging.WARNING,
             2:logging.INFO,
             3:logging.DEBUG}

    logger.setLevel(level[FLAGS.verbose])

    twoDcoordsToThreeDcoords(openpose_output_dir, "./output/image")

    # tf.app.run()
