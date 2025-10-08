import scipy.misc as sc
import matplotlib.pyplot as plt
import imageio.v2 as imageio

sc.imread=imageio.imread
sc.imsave=imageio.imwrite

im=sc.imread('zamalek.jpg')
sc.imsave('imagedzamalek.jpg',im)
plt.imshow(im)
plt.show()
