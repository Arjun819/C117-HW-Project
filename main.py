import cv2
import os
import shutil
import time
import sys

path = "Images"
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)

    for ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
width,height,channel = frame.shape
size = (width,height)

vid = cv2.VideoWriter("videoking.mp4",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0, count-1):
    cv2.imread(images[i])
    vid.write(frame)
    vid.release()
    print("done")
