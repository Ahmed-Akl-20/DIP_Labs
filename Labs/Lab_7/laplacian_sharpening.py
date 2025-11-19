import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('MET.jpg', cv2.IMREAD_GRAYSCALE)

l_edge = cv2.filter2D(img, -1, np.array(
    [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ], dtype=np.float32
))

l_sharpen = cv2.filter2D(img, -1, np.array(
    [
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=np.float32
))

sharpen = cv2.add(img, -l_sharpen)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(l_edge, cmap='gray')
plt.title('laplacian with center +4 image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(l_sharpen, cmap='gray')
plt.title('laplacian with center -4 image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(sharpen, cmap='gray')
plt.title('sharpened image')
plt.axis('off')

plt.show()
