# first I want to know how long a video is. 
# then I want to know how long all videos in a folder is. 

# second I want to run hand detection on the video.

# finally I want to visualize some good examples and bad examples such that I can evaluate the labeling. 

#STEP 1: video length
import ffmpeg # to read vid length
from pathlib import Path #to access files and folders
import time # to track efficiency/speed

def getVidLength(path):
    out = ffmpeg.probe(path)
    clip_length = float(out['streams'][0]['duration']) #returned as a string, must convert to float to be usable later on.
    return clip_length/60; # convert to minutes

def main():
    parent_folder = Path("/Volumes") #creates a Path object
    #finds all the SD cards currently being read by the computer
    for subdir in parent_folder.iterdir(): #calls method iterdir() that gets all the sub directories
        folder_name = subdir.name
        if "Untitled" in folder_name: #checks that its an SD card folder.
            video_folder = Path(f"/Volumes/{folder_name}/DCIM")
            vidlength = 0
            for video_files in video_folder.iterdir(): #gets all the clips on the SD card.
                vidlength += getVidLength(video_files)*10
            print(f"{folder_name} is {round(vidlength/60*10)/10} hours long" )

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    duration = end-start
    print(f"took {round(duration/60*10)/10} minutes")

# results from running the above
# zikangjiang@Zikangs-MacBook-Pro data-qc % python3 qc.py
# Untitled 2 is 7.759229722222224 hours long
# Untitled 1 is 7.446141388888889 hours long
# Untitled is 7.448672500000001 hours long
# took 107.08723092079163