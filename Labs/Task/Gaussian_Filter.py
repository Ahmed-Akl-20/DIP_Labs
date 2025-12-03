# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Read image (gray)

# img = cv2.imread('Lion.jpeg', 0)

# # FFT + Shift

# F = np.fft.fft2(img)
# Fshift = np.fft.fftshift(F)

# rows, cols = img.shape
# crow, ccol = rows//2, cols//2

# R = 50   # same radius like Ideal

# # --------- Gaussian Masks ---------

# # Low-Pass mask

# mask_LP = np.zeros((rows, cols), np.float32)

# for u in range(rows):
#     for v in range(cols):
#         D2 = (u - crow)**2 + (v - ccol)**2
# mask_LP[u, v] = np.exp(-D2 / (2 * (R**2)))

# # High-Pass = 1 - Low-Pass

# mask_HP = 1 - mask_LP

# # -----------------------------------

# # Apply masks

# F_LP = Fshift * mask_LP
# F_HP = Fshift * mask_HP

# # Inverse FFT

# img_LP = np.abs(np.fft.ifft2(np.fft.ifftshift(F_LP)))
# img_HP = np.abs(np.fft.ifft2(np.fft.ifftshift(F_HP)))

# # Show results

# plt.figure(figsize=(10,5))

# plt.subplot(1,2,1)
# plt.title("Gaussian Low Pass")
# plt.imshow(img_LP, cmap='gray')

# plt.subplot(1,2,2)
# plt.title("Gaussian High Pass")
# plt.imshow(img_HP, cmap='gray')

# plt.show()



import cv2
import numpy as np
import matplotlib.pyplot as plt

# ================================

# 1) Load image (grayscale)

# ================================

img = cv2.imread("Lion.jpeg", cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32)

# ================================

# 2) FFT + Shift

# ================================

F = np.fft.fft2(img)
F_shift = np.fft.fftshift(F)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

# Gaussian cutoff

D0 = 50

# ================================

# 3) Gaussian Low-Pass + High-Pass Masks

# ================================

LP = np.zeros((rows, cols), np.float32)

for u in range(rows):
    for v in range(cols):
        D2 = (u - crow)**2 + (v - ccol)**2
LP[u, v] = np.exp(-D2 / (2 * (D0**2)))

HP = 1 - LP

# ================================

# 4) Apply Masks

# ================================

F_LP = F_shift * LP
F_HP = F_shift * HP

# ================================

# 5) Inverse FFT

# ================================

img_LP = np.abs(np.fft.ifft2(np.fft.ifftshift(F_LP)))
img_HP = np.abs(np.fft.ifft2(np.fft.ifftshift(F_HP)))

# ================================

# 6) Show Results Side-by-Side

# ================================

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Gaussian LOW-PASS")
plt.imshow(img_LP, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Gaussian HIGH-PASS")
plt.imshow(img_HP, cmap='gray')
plt.axis('off')

plt.show()
