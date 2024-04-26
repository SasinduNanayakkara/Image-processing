import cv2
import numpy as np

image = cv2.imread('binary2.PNG', 0) # read image

kernel = np.ones((5,5), np.uint8) # create kernal

eroded_image1 = cv2.erode(image, kernel, iterations=1) # apply erode effect
eroded_image2 = cv2.erode(image, kernel, iterations=3)
eroded_image3 = cv2.erode(image, kernel, iterations=5)

cv2.imshow("original image", image) # display image
cv2.imshow("eroded image1", eroded_image1)
cv2.imshow("eroded image2", eroded_image2)
cv2.imshow("eroded image3", eroded_image3)

cv2.waitKey(0)


image2 = cv2.imread('binary.png', 0) # read image

kernel = np.ones((5,5), np.uint8)

dilated_image = cv2.dilate(image2, kernel, iterations=1) # apply to dilate effect

# Display the original and dilated images
cv2.imshow('Original Image', image2)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)


image3 = cv2.imread('binary4.png', 0) # read image

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image3, kernel, iterations=1)

opening = cv2.dilate(erosion, kernel, iterations=1)

cv2.imshow('Original Image', image3)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)

image4 = cv2.imread('binary5.png', 0)

kernel = np.ones((5,5), np.uint8)

closing = cv2.morphologyEx(image4, cv2.MORPH_CLOSE, kernel) # Perform dilation followed by erosion (Closing)

cv2.imshow('Original Image', image4)
cv2.imshow('Dilated Image', closing)
cv2.waitKey(0)

image5 = cv2.imread('binary6.PNG', 0)

kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(image5, kernel, iterations=3)

dilation = cv2.dilate(image5, kernel, iterations=1)

cv2.imshow('Original Image', image5)
cv2.imshow('Erosion Image', erosion)
cv2.imshow('Dilation image', dilation)
cv2.waitKey(0)
