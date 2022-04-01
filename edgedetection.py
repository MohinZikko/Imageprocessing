from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.feature import canny

img = io.imread("cells.jpg", as_gray=True)
edge_robert = roberts(img)
edge_sobel = sobel(img)
edge_scharr = scharr(img)
edge_prewitt = prewitt(img)
edge_canny = canny(img, sigma=2)

fig, axis = plt. subplots(nrows=3, ncols=2, sharex=True, sharey=True, figsize=(10, 14))

ax = axis.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title('Original Image')

ax[1].imshow(edge_robert, cmap=plt.cm.gray)
ax[1].set_title('robert Image')

ax[2].imshow(edge_sobel, cmap=plt.cm.gray)
ax[2].set_title('sobel Image')

ax[3].imshow(edge_scharr, cmap=plt.cm.gray)
ax[3].set_title('scharr Image')

ax[4].imshow(edge_prewitt, cmap=plt.cm.gray)
ax[4].set_title('prewitt Image')

ax[5].imshow(edge_canny, cmap=plt.cm.gray)
ax[5].set_title('canny Image')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
# plt.imshow(edge_canny, cmap= 'gray')
# plt.axis('off')