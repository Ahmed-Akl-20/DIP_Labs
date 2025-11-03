# Low Pass Spatial Domain Filtering (Average Blur)
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


img = Image.open("Back.jpg").convert("RGB")

# Convert PIL to NumPy array
img_array = np.array(img)
m, n, _ = img_array.shape

# Create 3×3 Averaging Filter
mask = np.ones((3, 3), dtype=float) / 9

# Output image
img_new = np.zeros((m, n), dtype=float)

# Apply filter manually (spatial convolution)
for i in range(1, m-1):
    for j in range(1, n-1):
        # خُد حوالي 3×3 من كل قناة (R, G, B)
        region = img_array[i-1:i+2, j-1:j+2, :]
        value = np.mean(region * mask[:, :, None])  # Mean of all 9*3 values
        img_new[i, j] = value

# Convert output to uint8
img_new = np.clip(img_new, 0, 255).astype(np.uint8)

# Display Results
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(img_new, cmap="gray")
plt.title("After 3×3 Average Filter")
plt.axis("off")

plt.tight_layout()
plt.show()
