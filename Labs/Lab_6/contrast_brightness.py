import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ---------- Load image ----------
img = Image.open("Back.jpg").convert("RGB")  
arr = np.array(img).astype(np.int32)   
H, W, C = arr.shape
print("Image shape:", arr.shape)

# ---------- 1. Brightness ----------
bias = 50
bright_manual = np.clip(arr + bias, 0, 255).astype(np.uint8)

# ---------- 2. Contrast Stretching ----------
in_min = arr.min()
in_max = arr.max()
print(f"Contrast stretch range: input min={in_min}, max={in_max}")

contrast_stretched = (arr - in_min) * 255.0 / (in_max - in_min)
contrast_stretched = np.clip(contrast_stretched, 0, 255).astype(np.uint8)

# ---------- Display ----------
plt.figure(figsize=(14,6))

plt.subplot(1,3,1)
plt.imshow(arr.astype(np.uint8))
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(bright_manual)
plt.title("Brightened")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(contrast_stretched)
plt.title("Contrast Stretched")
plt.axis("off")

plt.tight_layout()
plt.show()
