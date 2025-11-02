# first I want to know how long a video is. 
# then I want to know how long all videos in a folder is. 

# second I want to run hand detection on the video.

# finally I want to visualize some good examples and bad examples such that I can evaluate the labeling. 

#STEP 1: video length
import ffmpeg
from pathlib import Path #

def getVidLength(path):
    out = ffmpeg.probe(path)
    print(out['streams'][0]['duration'])

#as of 10:32pm, code TBD, will just read documentation later to figure out the optimal commands.
folder = Path("/Volumes/Untitled/DCIM")
items = list[Path](folder.iterdir())
print(items[:5])
print(len(items))

getVidLength('/Volumes/Untitled/DCIM/00232-0000.mp4')

