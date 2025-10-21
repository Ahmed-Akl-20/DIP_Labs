import numpy as np
import matplotlib.pyplot as plt
from skimage import color, transform
from skimage.util import img_as_float
from scipy.linalg import hadamard
import cv2

# قراءة الصورة
img_color = cv2.imread('Zam.jpg')   # لو الصورة جنب الكود
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

# تحويلها لصورة رمادية
image = color.rgb2gray(img_color)
image = img_as_float(image)

# تصغير الصورة لحجم مناسب (256x256)
N = 256
image_resized = transform.resize(image, (N, N), anti_aliasing=True)

# إنشاء مصفوفة Hadamard
H = hadamard(N)

# تطبيق Walsh-Hadamard Transform
WHT = H @ image_resized @ H.T

# حساب المقدار (Magnitude)
magnitude = np.log(1 + np.abs(WHT))

# عرض النتائج
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_resized, cmap='gray')
plt.title("Original Image (Spatial Domain)")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(magnitude, cmap='gray')
plt.title("Walsh-Hadamard Transform (WHT Domain)")
plt.axis('off')

plt.tight_layout()
plt.show()
