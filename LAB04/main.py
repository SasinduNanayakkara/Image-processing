import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("darkImage.png", 0) # read the image

hist1 = cv2.calcHist([image], [0], None, [256], [0, 256]) # calculate histogram for the image

equ = cv2.equalizeHist(image) # Apply histogram equalization

res = np.hstack((image, equ)) # joining multiple numpy array

cv2.imshow("image", res) # display image
cv2.waitKey(0)

hist2 = cv2.calcHist([res], [0], None, [256], [0, 256]) # calculate histogram for the

plt.subplot(1,3,1), plt.plot(hist1) # implement a subplot for both diagrams
plt.subplot(1,3,3), plt.plot(hist2)
plt.show() # display diagrams

image2 = cv2.imread("brightImage.png", 0)

hist3 = cv2.calcHist([image2], [0], None, [256], [0, 256])

equ2 = cv2.equalizeHist((image2))

res2 = np.hstack((image2, equ2))
cv2.imshow("image 2 ", res2)
cv2.waitKey(0)

hist4 = cv2.calcHist([res2], [0], None, [256], [0, 256])

plt.subplot(1,3,1), plt.plot(hist3)
plt.subplot(1,3,3), plt.plot(hist4)
plt.show()

