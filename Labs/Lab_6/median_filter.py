# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# # Read image
# img = Image.open("Back.jpg").convert("RGB")  
# arr = np.array(img)

# # Image dimensions
# m, n, c = arr.shape

# # Create empty output image
# new_img = np.zeros_like(arr, dtype=np.uint8)

# # Median Filter (3x3)
# for k in range(c):             # لكل قناة (R, G, B)
#     for i in range(1, m - 1):  # متجنب الحواف
#         for j in range(1, n - 1):
#             # اجمع الـ 9 قيم المحيطة بالبكسل
#             neighbors = [
#                 arr[i-1, j-1, k], arr[i-1, j, k], arr[i-1, j+1, k],
#                 arr[i,   j-1, k], arr[i,   j, k], arr[i,   j+1, k],
#                 arr[i+1, j-1, k], arr[i+1, j, k], arr[i+1, j+1, k]
#             ]
#             # رتبهم، واختار المتوسط (الوسيط)
#             neighbors = sorted(neighbors)
#             new_img[i, j, k] = neighbors[4]

# # Display results
# plt.figure(figsize=(10,5))

# plt.subplot(1,2,1)
# plt.imshow(arr)
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1,2,2)
# plt.imshow(new_img)
# plt.title("Median Filter (3x3)")
# plt.axis("off")

# plt.tight_layout()
# plt.show()

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Read image
img = Image.open("images/1.jpg").convert("RGB")
arr = np.array(img)

# Get image dimensions
m, n, c = arr.shape

# Create output image
new_img = np.zeros_like(arr, dtype=np.uint8)

# Median Filter (3x3)
for k in range(c):             # لكل قناة لون (R, G, B)
    for i in range(1, m - 1):  # هنمشي على الصفوف
        for j in range(1, n - 1):  # و الأعمدة (مع تجاهل الحواف)
            
            # جمع الـ 9 قيم المحيطة بالبكسل
            new_val = [
                arr[i-1, j-1, k], arr[i-1, j, k], arr[i-1, j+1, k],
                arr[i,   j-1, k], arr[i,   j, k], arr[i,   j+1, k],
                arr[i+1, j-1, k], arr[i+1, j, k], arr[i+1, j+1, k]
            ]
            
            # ترتيب القيم واختيار القيمة المتوسطة (Median)
            new_val = sorted(new_val)
            new_img[i, j, k] = new_val[4]

# Display
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(arr)
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(new_img)
plt.title("Median Filter (3x3)")
plt.axis("off")

plt.tight_layout()
plt.show()
