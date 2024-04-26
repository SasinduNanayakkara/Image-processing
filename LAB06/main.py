import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('saltandpepper1.png', 0) # read image

kernel = np.ones((5,5), np.float32) / 25 # calculate the kernal
dst = cv2.filter2D(image, -1, kernel) # apply filter2D

result = np.hstack((image, dst)) # set the images side by side
cv2.imshow("result", result) # display image

cv2.waitKey(0)

# =================================================================================

image2 = cv2.imread('saltandpepper2.png', 0) # read image

dst = cv2.blur(image2, (3, 3)) # apply blur effect (box filter)

result = np.hstack((image2, dst)) # set the images side by side

cv2.imshow("result", result) # display image
cv2.waitKey(0)

# ======================================================================================

image3 = cv2.imread('gaussian Noise.png', 0) # read image

median = cv2.medianBlur(image3, 3) # apply median blur effect

medianResult = np.hstack((image3, median)) # set the images side by side

cv2.imshow("result", medianResult) # display image
cv2.waitKey(0)

# ======================================================================================

gaussianBlur = cv2.GaussianBlur(image3, (11, 11), 0) # apply gaussian effect

result = np.hstack((image3, gaussianBlur)) # set the images side by side

cv2.imshow("result", result) # display image
cv2.waitKey(0)

# ======================================================================================

image4 = cv2.imread('hubble.png', 0) # read image

kernel = np.ones((15,15), np.float32) / 225 # calculate kernel

dst = cv2.filter2D(image4, -1, kernel) # apply blur effect with filter2D

_, binaryImage = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # create binary image using threshold

contours, _ = cv2.findContours(binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find contours in the binary image

largest_contour = max(contours, key=cv2.contourArea) # Find the contour with the largest area

mask = np.zeros_like(image4) # Create a mask using the largest contour
cv2.drawContours(mask, [largest_contour], -1, (255,255,255), thickness=cv2.FILLED)

highlited_image = cv2.bitwise_and(image4, mask) # Apply the mask to the original image

result = np.hstack((image4, dst, highlited_image)) # set the images side by side

cv2.imshow("result", result) # diplay image
cv2.waitKey(0)

