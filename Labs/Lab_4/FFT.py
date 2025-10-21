import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import color
from skimage.util import img_as_float

# اقرأ الصورة
img = cv2.imread('profile.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# حوّلها لصورة رمادية وfloat
image = color.rgb2gray(img)
image = img_as_float(image)

# تطبيق تحويل فورييه (FFT)
F = np.fft.fft2(image)
Fshift = np.fft.fftshift(F)  # نقل المكونات منخفضة التردد للمنتصف

# استخراج المكونات
magnitude = np.abs(Fshift)
phase = np.angle(Fshift)
real_part = np.real(Fshift)
imag_part = np.imag(Fshift)
log_magnitude = np.log(1 + magnitude)

# عرض النتائج
plt.figure(figsize=(12, 10))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image (Spatial Domain)')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(real_part, cmap='gray')
plt.title('Real Part of FFT')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(imag_part, cmap='gray')
plt.title('Imaginary Part of FFT')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(log_magnitude, cmap='gray')
plt.title('Log Magnitude Spectrum')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(phase, cmap='gray')
plt.title('Phase Spectrum')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(np.log(1 + np.abs(Fshift)), cmap='inferno')
plt.title('Magnitude (Colored for Clarity)')
plt.axis('off')

plt.tight_layout()
plt.show()
