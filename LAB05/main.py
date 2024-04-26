import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("apples.jpg", 1) # read image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert color

plt.imshow(image) # show the image
plt.show()

image_negative = cv2.bitwise_not(image) # convert the image into negative

plt.imshow(image_negative) # display negative image
plt.show()

# ======================================================================================

image2 = cv2.imread('gamma.jpg', 0) # read image
# image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

plt.imshow(image2, cmap='gray') # display image with gray values
plt.show()

gamma = 0.4
image_gamma = np.power(image2, gamma) # apply power-law transformation calculation

plt.imshow(image_gamma, cmap='gray') # display transformed image
plt.show()

# =======================================================================================

gamma = 0.4

transformed_image = np.power(image2 / 255.0, gamma) * 255.0  # apply power-law transformation calculation

plt.imshow(transformed_image, cmap='gray') # display transformed image
plt.show()

plt.subplot(1, 2, 1) # display both images in same window
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_GRAY2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(transformed_image, cmap='gray')
plt.title('Transformed Image (Gamma = {})'.format(gamma))
plt.axis('off')
plt.show()

# ==============================================================================================

image3 = cv2.imread("log.jpg", 0) # read image

c = 255 / np.log(1 + np.max(image3)) # calculates a scaling factor (c) for the logarithmic transformation
log_transmormed_image = c * (np.log(image3 + 1))

plt.subplot(1, 2, 1) # display both images in same window
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB), cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(log_transmormed_image, cmap='gray')
plt.title('Log Transformed Image')
plt.axis('off')

plt.show()

