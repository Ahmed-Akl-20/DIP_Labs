import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

# قراءة الصورة
im = imread('Lab_3/UWK.jpg')

# لو الصورة من نوع uint8 نحولها لقيم من 0 إلى 1
if im.dtype == np.uint8:
    im = im / 255.0

# Downsampling (تقليل الحجم)
d = im[::4, ::4, :]

# Upsampling (تكبير الصورة)
u = np.repeat(np.repeat(d, 4, axis=0), 4, axis=1)

# ضبط الحجم علشان يطابق الأصل في العرض
u = u[:im.shape[0], :im.shape[1], :]

# عرض الصور
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(im)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(d)
plt.title('Downsampled Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(u)
plt.title('Upsampled Image')
plt.axis('off')

plt.show()
