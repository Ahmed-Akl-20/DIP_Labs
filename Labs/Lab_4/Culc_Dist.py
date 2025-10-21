import numpy as np

import matplotlib.pyplot as plt

import cv2

import math

#create image

image = np.zeros((28,28,3), np.uint8)

# Choose red pixel location

image [10,15] = [255,0,0]

# Choose green pixel location

image [21,23] = [0,255,0]

# Save image

cv2.imwrite('1.png', image)

plt.imshow(image)

# Finding distance between the pixels

x1,y1, x2, y2 = 10,15,21,23

print("Distance:", math.sqrt((x2-x1)*2 + (y2-y1)*2))


