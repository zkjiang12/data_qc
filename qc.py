
#for getting vid length
import ffmpeg # to read vid length
from pathlib import Path #to access files and folders
import time # to track efficiency/speed
import os

def getVidLengthFFMPEG(path):
    out = ffmpeg.probe(path) #ffmpeg.probe() returns 
    print(out)
    print()
    clip_length = float(out['streams'][0]['duration']) #returned as a string, must convert to float to be usable later on.
    return clip_length/60 # convert to minutes

def getVidLengthOS(file_name):
    size = os.path.getsize(file_name)
    print(file_name)
    print(round(size/1000000*10)/10)
    print()
    # print()
    # clip_length = float(out['streams'][0]['duration']) #returned as a string, must convert to float to be usable later on.
    # return clip_length/60 # convert to minutes


#main QC code that loops through the SD cards and runs QC on each video. 
def main():
    parent_folder = Path("/Volumes") #creates a Path object pointing to the /Volumes folder

    for subdir in parent_folder.iterdir(): #iterdir() gets all the sub directories of the Volume folder. finds all SD cards being read by the computer. 
        container_folder_name = subdir.name

        if "Untitled" not in container_folder_name: # if folder name does not contains Untitled not one of our SD cards
            continue

        video_folder = Path(f"/Volumes/{container_folder_name}/DCIM") # path to the folder which contains all clips on the SD card
        vidlength = 0
        {getVidLengthOS(video_files) for video_files in video_folder.iterdir()}       
         # vidlength += {getVidLengthFFMPEG(video_files) for video_files in video_folder.iterdir()} #goes through all clips in the folder 

        print()
        print(f"{container_folder_name} is {round(vidlength/60*10)/10} hours long" )
        print()

#only runs if this is the file being run, not imported into another file. 
#really just added it here for vibes to make the code look nicer.
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    duration = end - start
    print(f"took {round(duration/60*10)/10} minutes")

# {'streams': [{'index': 0, 'codec_name': 'h264', 'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10', 'profile': 'High', 'codec_type': 'video', 'codec_tag_string': 'avc1', 'codec_tag': '0x31637661', 'width': 1920, 'height': 1080, 'coded_width': 1920, 'coded_height': 1080, 'has_b_frames': 0, 'pix_fmt': 'yuv420p', 'level': 41, 'field_order': 'progressive', 'refs': 1, 'is_avc': 'true', 'nal_length_size': '4', 'id': '0x1', 'r_frame_rate': '30/1', 'avg_frame_rate': '30/1', 'time_base': '1/1000', 'start_pts': 0, 'start_time': '0.000000', 'duration_ts': 180000, 'duration': '180.000000', 'bit_rate': '8352023', 'bits_per_raw_sample': '8', 'nb_frames': '5400', 'extradata_size': 54, 'disposition': {'default': 1, 'dub': 0, 'original': 0, 'comment': 0, 'lyrics': 0, 'karaoke': 0, 'forced': 0, 'hearing_impaired': 0, 'visual_impaired': 0, 'clean_effects': 0, 'attached_pic': 0, 'timed_thumbnails': 0, 'non_diegetic': 0, 'captions': 0, 'descriptions': 0, 'metadata': 0, 'dependent': 0, 'still_image': 0, 'multilayer': 0}, 'tags': {'creation_time': '2002-10-29T03:32:30.000000Z', 'language': 'eng', 'handler_name': 'VideoHandler', 'vendor_id': 'SUNP'}}, {'index': 1, 'codec_name': 'pcm_s16le', 'codec_long_name': 'PCM signed 16-bit little-endian', 'codec_type': 'audio', 'codec_tag_string': 'sowt', 'codec_tag': '0x74776f73', 'sample_fmt': 's16', 'sample_rate': '16000', 'channels': 1, 'bits_per_sample': 16, 'initial_padding': 0, 'id': '0x2', 'r_frame_rate': '0/0', 'avg_frame_rate': '0/0', 'time_base': '1/16000', 'start_pts': 0, 'start_time': '0.000000', 'duration_ts': 2880000, 'duration': '180.000000', 'bit_rate': '256000', 'nb_frames': '2880000', 'disposition': {'default': 1, 'dub': 0, 'original': 0, 'comment': 0, 'lyrics': 0, 'karaoke': 0, 'forced': 0, 'hearing_impaired': 0, 'visual_impaired': 0, 'clean_effects': 0, 'attached_pic': 0, 'timed_thumbnails': 0, 'non_diegetic': 0, 'captions': 0, 'descriptions': 0, 'metadata': 0, 'dependent': 0, 'still_image': 0, 'multilayer': 0}, 'tags': {'creation_time': '2002-10-29T03:32:30.000000Z', 'language': 'eng', 'handler_name': 'SoundHandler', 'vendor_id': '[0][0][0][0]'}}], 'format': {'filename': '/Volumes/Untitled 12/DCIM/00057-0011.mp4', 'nb_streams': 2, 'nb_programs': 0, 'nb_stream_groups': 0, 'format_name': 'mov,mp4,m4a,3gp,3g2,mj2', 'format_long_name': 'QuickTime / MOV', 'start_time': '0.000000', 'duration': '180.000000', 'size': '193754112', 'bit_rate': '8611293', 'probe_score': 100, 'tags': {'major_brand': 'qt  ', 'minor_version': '512', 'compatible_brands': 'qt  ', 'creation_time': '2025-02-26T09:09:48.000000Z'}}}


#####OLD CODE
#####OLD CODE
#####OLD CODE
#####OLD CODE
#####OLD CODE
#####OLD CODE
#####OLD CODE
#####OLD CODE
# #for doing hand detection
# import mediapipe as mp
# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision
# import cv2
# import random

# def load_model():
#     model_path = "/Users/zikangjiang/data-qc/hand_landmarker.task"

#     # STEP 2: Create an HandLandmarker object.
#     base_options = python.BaseOptions(model_asset_path=model_path)
#     options = vision.HandLandmarkerOptions(base_options=base_options,
#                                         num_hands=2)
#     detector = vision.HandLandmarker.create_from_options(options)
#     return detector

# def detectHands(vidPath,detector): # this is the core part of the QC. goal is a percentage of frames with hands detected.
#     print(f'running hand detection on {vidPath}')

#     # Use OpenCV’s VideoCapture to load the input video.
#     clip = cv2.VideoCapture(vidPath)

#     # Loop through each frame in the video using VideoCapture#read()
#     hands = 0
#     frames = 0
#     while True:
#         #read the video
#         ret, frame = clip.read()     

#         #if no more frames in the video
#         if ret == False:
#             break;   

#          # need to sample 7% of the population to get 95% CL 
#         random_integer = random.randint(1, 100)

#         if random_integer > 6: #only run hand detection on 7% of the samples. 
#             continue

#         #need to convert image into an Image object that can be used in media pipe
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame_rgb = cv2.resize(frame_rgb, (192, 192))
#         mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb) 

#         #run the detection model
#         detection_result = detector.detect(mp_image)

#         #if the response is not empty.
#         if len(detection_result.handedness) != 0:
#             hands += 1
        
#         frames += 1

#     return hands/frames

# #code I wrotte since I thought the above hand detection wasn't working. 
# #it's pretty similar to the above, you don't need to download a model, but also the output has a worse format.
# def detectHandsv2(vidPath):
#     mp_pose = mp.solutions.pose
#     pose = mp_pose.Pose()

#     # Use OpenCV’s VideoCapture to load the input video.
#     clip = cv2.VideoCapture(vidPath)

#     while True:
#         #read the video
#         ret, frame = clip.read()     

#         if ret == False:
#             break;   

#         # Convert the frame to RGB
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # Process the frame with MediaPipe Pose
#         result = pose.process(frame_rgb)
#         print(result)
#         if result.pose_landmarks:
#             print(result.pose_landmarks.landmark)
