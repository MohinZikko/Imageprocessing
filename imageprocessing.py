from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean
from matplotlib import pyplot as plt

img = io.imread("image.jpg", as_gray=True)
rescaled_img = rescale(img, 1.0/4.0, anti_aliasing=True)
resized_img = resize(img, (400,400))
down_img = downscale_local_mean(img, (4, 3))
plt.imshow(down_img)
plt.show()