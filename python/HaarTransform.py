import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rescale(im):
    return im / im.max()

def toGreyscale(im):
    def product(a):
        p = 1
        for x in a: p *= x
        return p

    grey_im = np.zeros((len(im), len(im[0])), dtype = np.float32)
    for i in range(len(im)):
        for j in range(len(im[0])):
            grey_im[i][j] = product(im[i][j])
    m = np.max(grey_im)
    grey_im = rescale(grey_im)
    return grey_im

def padImage(im):
    # The 4 is chosen here as the size of the subsets of the image to apply the compression to.
    n = math.ceil(max(im.shape) / 4) * 4
    padded_im = np.zeros((n, n))
    for i in range(len(im)):
        for j in range(len(im[0])):
            padded_im[i][j] = im[i][j]
    return padded_im

def HaarTransform(im, threshold):
    original_shape = (im.shape[0], im.shape[1])
    transformed = padImage(toGreyscale(im))
    W1 = np.asarray([[0.5, 0, 0.5, 0], [0.5, 0, -0.5, 0], [0, 0.5, 0, 0.5], [0, 0.5, 0, -0.5]])
    W2 = np.asarray([[0.5, 0.5, 0, 0], [0.5, -0.5, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    n = len(transformed)
    for i in range(0, n + 1 - 4, 4):
        for j in range(0, n + 1 - 4, 4):
            subset = np.zeros((4, 4))
            for a in range(4):
                for b in range(4):
                    subset[a][b] = transformed[i + a][j + b]
            new_subset = np.dot(np.dot(W2.T, W1.T), np.dot(subset, np.dot(W1, W2)))
            for a in range(4):
                for b in range(4):
                    if abs(new_subset[a][b]) <= threshold:
                        new_subset[a][b] = 0.0
            new_subset = np.dot(np.dot(W1, W2), np.dot(new_subset, np.dot(W2.T, W1.T)))
            for a in range(4):
                for b in range(4):
                    transformed[i + a][j + b] = new_subset[a][b]
    new_transformed = np.zeros(original_shape, dtype = np.float32)
    for i in range(original_shape[0]):
        for j in range(original_shape[1]):
            new_transformed[i][j] = abs(transformed[i][j])
    return rescale(new_transformed)

im = mpimg.imread('test_image.jpg')
fig, axes = plt.subplots(2, 3)
fig.suptitle("Haar Transform Demo")
axes[0][0].imshow(toGreyscale(im), cmap = 'gray')
axes[0][0].set_title('Original Image')
i = 1
j = 0
for threshold in [0.01, 0.05, 0.1, 0.15, 0.2]:
    new_im = HaarTransform(im, threshold)
    axes[j][i].imshow(new_im, cmap = 'gray')
    axes[j][i].set_title('Threshold = ' + str(threshold))
    i += 1
    if i == 3:
        i = 0
        j += 1
plt.show()
