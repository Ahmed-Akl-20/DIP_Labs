import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Lion.jpeg', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows//2, cols//2
R = 50

mask_LP = np.zeros((rows, cols), np.uint8)
for u in range(rows):
    for v in range(cols):
        if np.sqrt((u-crow)**2+ (v-ccol)**2) <= R:
            mask_LP[u, v] = 1

mask_HP = np.ones((rows, cols), np.uint8)
for u in range(rows):
    for v in range(cols):
        if np.sqrt((u-crow)**2 + (v-ccol)**2) <= R:
            mask_HP[u, v] = 0

fshift_LP = fshift * mask_LP
fshift_HP = fshift * mask_HP

f_ishift_LP = np.fft.ifftshift(fshift_LP)
img_LP = np.abs(np.fft.ifft2(f_ishift_LP))
f_ishift_HP = np.fft.ifftshift(fshift_HP)
img_HP = np.abs(np.fft.ifft2(f_ishift_HP))

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Ideal Low Pass")
plt.imshow(img_LP, cmap ='gray')

plt.subplot(1,2,2)
plt.title("Ideal High Pass")
plt.imshow(img_HP, cmap ='gray')

plt.show()