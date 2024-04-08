import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)  # print all the color-space conversion methods in OpenCV.

img = cv2.imread('1.png', 1) # read the image

cv2.imshow('img', img) # display image with name
cv2.waitKey() # display the image until it close

video = cv2.VideoCapture("1.mov") # read the video
while {video.isOpened()}: # loop the code until video open
    ret, frame = video.read() # read the video frame by frame
    resized = cv2.resize(frame, (300, 200)) # resize the video output
    hsVideo = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV) # change the video color into HSV
    lower = np.array([110, 50, 50]) # define lower level of the color using numpy
    heigher = np.array([130, 255, 255]) # define higher level of the color using numpy
    mask = cv2.inRange(hsVideo, lower, heigher) # define specific color range for the video
    result = cv2.bitwise_and(resized, resized, mask=mask) # create a video with specific color range [blue]
    cv2.imshow('normal video', resized) # display actual video
    cv2.imshow('video 1', mask)  # display black and white video (the given range is blue color area so )
    cv2.imshow('video2', hsVideo) # display HSV converted video
    cv2.imshow('video3', result) # display all the blue color areas and other will be black
    if cv2.waitKey(1) & 0xFF == ord('q'): # stop the video when user enter the "q" letter
        break

video.release()
cv2.destroyAllWindows()


