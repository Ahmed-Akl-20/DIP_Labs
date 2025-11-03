import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ---------- Load image ----------
img = Image.open("Back.jpg").convert("RGB")
arr = np.array(img)   # shape (H, W, 3)
H, W, C = arr.shape
print("Image shape:", arr.shape)

# ---------- Method 1: vectorized (array math) ----------
# Brightness factor
bias = 50
bright_arr = arr.astype(np.int32) + bias
bright_arr = np.clip(bright_arr, 0, 255).astype(np.uint8)

# ---------- Method 2: pixel-by-pixel loop (manual way) ----------
bright_manual = np.zeros_like(arr, dtype=np.uint8)

for i in range(H):
    for j in range(W):
        for k in range(C):
            new_val = arr[i, j, k] + bias
            # clamp 0–255
            if new_val > 255:
                new_val = 255
            elif new_val < 0:
                new_val = 0
            bright_manual[i, j, k] = new_val

# ---------- Display ----------
plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(arr)
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(bright_arr)
plt.title("Brightened (array math)")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(bright_manual)
plt.title("Brightened (pixel by pixel)")
plt.axis("off")

plt.tight_layout()
plt.show()