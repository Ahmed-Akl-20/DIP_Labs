import matplotlib.pyplot as plt
import numpy as np
import cv2

# قراءة الصورة بالدرجات الرمادية
img = cv2.imread('ahmed_akl.jpg', cv2.IMREAD_GRAYSCALE)

# تصغيرها لـ 256x256
img = cv2.resize(img, (256, 256))

# دالة لعرض الصور
def show(title, image):
    plt.figure(figsize=(4, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(title)
    plt.show()

# الصورة السالبة (Negative)
negative = 255 - img
show('Negative Image', negative)

# Threshold
thres_val = 120
_, thresv = cv2.threshold(img, thres_val, 255, cv2.THRESH_BINARY)
show('Threshold Image', thresv)

# Logarithmic Transform
c = 255 / np.log(1 + np.max(img))
s = c * (np.log(1 + img))
s = np.array(s, dtype=np.uint8)
show('Logarithmic Image', s)

# Gamma Correction
g = 0.5
normalize = img / 255.0
pw = np.power(normalize, g)
pw = np.uint8(pw * 255)
show('Gamma Image', pw)

# Gray Level Slicing
low, high = 100, 180
sliced = np.where((img > low) & (img < high), 255, 0)
show('Gray Level Slicing (Range 100-180)', sliced)

# Bit Plane Slicing
bit_planes = []
for i in range(8):
    b = np.bitwise_and(img, 1 << i)
    b = np.uint8(b * 255 / (1 << i))
    bit_planes.append(b)

plt.figure(figsize=(10, 5))
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(bit_planes[i], cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')

plt.tight_layout()
plt.show()
