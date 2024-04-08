import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("sunflower.jpg", 0) # read the image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # convert the color of the image (blue, green, red to red, green, blue)
plt.show() # display the plot

hist = cv2.calcHist([image], [0], None, [256], [0, 256]) # calculate histogram of the image(blue channel of the image)
plt.plot(hist) # plot the calculated histogram
plt.show() # display the histogram

plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # create a subplot with image
plt.subplot(122), plt.plot(hist) # create subplot with histogram graph
plt.show() # display both in one plot

image2 = cv2.imread("sunflower.jpg", 1) # read the image
color = ('b', 'g', 'r') # define color array
for i, col in enumerate(color): # initiates a loop that iterates over each color component in the tuple color, assigning the index to i and the color character to col.
    histogram = cv2.calcHist([image2], [i], None, [256], [0, 256]) # create histogram
    plt.plot(histogram, color = col) # create the plot using calculated values
    plt.xlim([0, 255]) # sets the limit of the x-axis of the plot from 0 to 255, which represents the range of pixel values.
plt.show() # displays the histogram of the blue, green, and red color channels of the input image "sunflower.jpg".
