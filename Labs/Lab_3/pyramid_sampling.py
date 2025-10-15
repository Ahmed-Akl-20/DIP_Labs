import cv2
import matplotlib.pyplot as plt

# قراءة الصورة
im = cv2.imread('Lab_3/UWK.jpg')

# تحويل الألوان من BGR إلى RGB
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# تقليل حجم الصورة مرتين
d1 = cv2.pyrDown(im)
d2 = cv2.pyrDown(d1)

# تكبير الصورة مرتين
u1 = cv2.pyrUp(d2)
u2 = cv2.pyrUp(u1)

# عرض الصور
images = [im, d1, d2, u1, u2]
titles = ['Original Image' , 'ds1' , 'ds2' , 'us1' , 'us2']

plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()
