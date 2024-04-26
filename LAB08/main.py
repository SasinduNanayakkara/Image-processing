import cv2
import numpy as np

image = cv2.imread('building.jpg', 0)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate first image derivatives
first_image_derivatives = np.sqrt(sobel_x**2 + sobel_y**2)

# Apply the Sobel operator for second order derivatives
sobel_xx = cv2.Sobel(image, cv2.CV_64F, 2, 0, ksize=3)
sobel_yy = cv2.Sobel(image, cv2.CV_64F, 0, 2, ksize=3)
sobel_xy = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=3)

# Calculate second image derivatives
second_image_derivatives = sobel_xx + sobel_yy

# Display the results or save them to files as needed
cv2.imshow('First Image Derivatives', first_image_derivatives.astype(np.uint8))
cv2.imshow('Second Image Derivatives', second_image_derivatives.astype(np.uint8))
cv2.waitKey(0)

# =========================================================================================

blur_image = cv2.GaussianBlur(image, (3,3), 0) # apply gaussian blur effect

dst = cv2.Laplacian(blur_image, cv2.CV_64F) # compute laplacian of the gaussian effect

dst = cv2.convertScaleAbs(dst) # covert to unit8

cv2.imshow('result', dst) # display image
cv2.waitKey(0)