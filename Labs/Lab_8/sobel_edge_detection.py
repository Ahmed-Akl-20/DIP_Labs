import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Palestine.jpg', cv2.IMREAD_GRAYSCALE)

x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# magnitude
mag = np.sqrt((x**2) + (y**2))
mag = np.uint8(255 * mag / np.max(mag))

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(np.abs(x), cmap='gray')
plt.title('Sobel X (Horizontal Image)')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(np.abs(y), cmap='gray')
plt.title('Sobel Y (Vertical Image)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(mag, cmap='gray')
plt.title('Sobel Magnitude')
plt.axis('off')

plt.tight_layout()
plt.show()
