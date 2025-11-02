# first I want to know how long a video is. 
# then I want to know how long all videos in a folder is. 

# second I want to run hand detection on the video.

# finally I want to visualize some good examples and bad examples such that I can evaluate the labeling. 

#for getting vid length
import ffmpeg # to read vid length
from pathlib import Path #to access files and folders
import time # to track efficiency/speed

#for doing hand detection
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2

def getVidLength(path):
    out = ffmpeg.probe(path)
    clip_length = float(out['streams'][0]['duration']) #returned as a string, must convert to float to be usable later on.
    return clip_length/60; # convert to minutes

def detectHands(vidPath): # this is the core part of the QC. goal is a percentage of frames with hands detected.
    print(f'running hand detection on {vidPath}')
    model_path = "/Users/zikangjiang/data-qc/hand_landmarker.task"

    # STEP 2: Create an HandLandmarker object.
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(base_options=base_options,
                                        num_hands=2)
    detector = vision.HandLandmarker.create_from_options(options)

    # Use OpenCV’s VideoCapture to load the input video.
    clip = cv2.VideoCapture(vidPath)

    # Loop through each frame in the video using VideoCapture#read()
    frame_index = 0
    while True:
        #read the video
        ret, frame = clip.read()     

        if ret == False:
            break;   

        #need to convert image into an Image object that can be used in media pipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb = cv2.resize(frame_rgb, (192, 192))
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb) 
        detection_result = detector.detect(mp_image,)
        print(detection_result)

        frame_index += 1

def detectHandsv2(vidPath):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Use OpenCV’s VideoCapture to load the input video.
    clip = cv2.VideoCapture(vidPath)

    while True:
        #read the video
        ret, frame = clip.read()     

        if ret == False:
            break;   

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Pose
        result = pose.process(frame_rgb)
        print(result)
        if result.pose_landmarks:
            print(result.pose_landmarks.landmark)

def main():
    parent_folder = Path("/Volumes") #creates a Path object
    #finds all the SD cards currently being read by the computer
    for subdir in parent_folder.iterdir(): #calls method iterdir() that gets all the sub directories
        folder_name = subdir.name
        if "Untitled" in folder_name: #checks that its an SD card folder.
            video_folder = Path(f"/Volumes/{folder_name}/DCIM")
            vidlength = 0
            for video_files in video_folder.iterdir(): #gets all the clips on the SD card.
                print(video_files)
                print(type(video_files))
                detectHands(video_files)
                vidlength += getVidLength(video_files)*10
            print(f"{folder_name} is {round(vidlength/60*10)/10} hours long" )

if __name__ == "__main__":
    start = time.time()
    print("starting")
    main()
    end = time.time()
    duration = end - start
    print(f"took {round(duration/60*10)/10} minutes")

# results from running the above
# zikangjiang@Zikangs-MacBook-Pro data-qc % python3 qc.py
# Untitled 2 is 7.759229722222224 hours long
# Untitled 1 is 7.446141388888889 hours long
# Untitled is 7.448672500000001 hours long
# took 107.08723092079163