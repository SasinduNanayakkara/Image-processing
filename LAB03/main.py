import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("sunflower.jpg", 0) # read the image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # convert the color of the image (blue, green, red to red, green, blue)
plt.show() # display the plot

hist = cv2.calcHist([image], [0], None, [256], [0, 256]) # calculate histogram of the image(blue channel of the image)
plt.plot(hist) # plot the calculated histogram
plt.show() # display the histogram

plt.subplot(1,3,1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # create a subplot with image
plt.subplot(1,3,3), plt.plot(hist) # create subplot with histogram graph
# plt.plot(no of nows, number of columns, element position)
plt.show() # display both in one plot


image2 = cv2.imread("sunflower.jpg", 1) # read the image
color = ('b', 'g', 'r') # define color array
for i, col in enumerate(color): # initiates a loop that iterates over each color component in the tuple color, assigning the index to i and the color character to col.
    histogram = cv2.calcHist([image2], [i], None, [256], [0, 256]) # create histogram
    plt.plot(histogram, color = col) # create the plot using calculated values
    plt.xlim([0, 255]) # sets the limit of the x-axis of the plot from 0 to 255, which represents the range of pixel values.
plt.show() # displays the histogram of the blue, green, and red color channels of the input image "sunflower.jpg".



# generate a histogram using numpy
b, g, r = cv2.split(image2)

hist1, bins = np.histogram(b.ravel(), 256, [0, 256]) # create histogram using specific array
hist2, bins = np.histogram(g.ravel(), 256, [0, 256])

# generate histogram using matpotlib
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 356, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

mask = np.zeros(image2.shape[:2], np.uint8) # creates a mask with the same dimensions as image2
mask[50:300, 250:400] = 255 # we have given the pixel range = assign it to white (50:300 x axis range, 250:400 - y axis range)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.show()

colorV = ('b', 'g', 'r')
for i, col in enumerate(colorV):
    hist4 = cv2.calcHist([image2], [i], None, [256], [0,256])
    plt.plot(hist4, colorV = col)
    plt.xlim([0, 255])

plt.show()