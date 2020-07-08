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

# Note that kernel_size must be an odd number so that the center of the kernel is a single number
def padImage(im, kernel_size, mode = 0):
    if mode == 0:
        k = (kernel_size - 1) // 2
        padded_im = np.zeros((im.shape[0] + kernel_size - 1, im.shape[1] + kernel_size - 1))
        for i in range(k, k + len(im)):
            for j in range(k, k + len(im[0])):
                padded_im[i][j] = im[i - k][j - k]
    else:
        k = (kernel_size - 1) // 2
        padded_im = np.zeros((im.shape[0] + kernel_size - 1, im.shape[1] + kernel_size - 1, 3))
        for i in range(k, k + len(im)):
            for j in range(k, k + len(im[0])):
                for channel in range(3):
                    padded_im[i][j][channel] = im[i - k][j - k][channel]
    return padded_im

def applyKernel(im, kernel, mode = 0):
    def convolve(subset, kernel):
        x = 0
        for i in range(len(subset)):
            for j in range(len(subset)):
                x += subset[i][j] * kernel[i][j]
        return x

    kernel_size = len(kernel)
    # Mode = 0 is greyscale images. Otherwise use color.
    if mode == 0:
        original_shape = (im.shape[0], im.shape[1], 3)
        padded = padImage(toGreyscale(im), kernel_size, mode)
        k = (kernel_size - 1) // 2
        convolved = np.zeros((padded.shape[0], padded.shape[1]), dtype = np.float32)
        for i in range(padded.shape[0] - kernel_size + 1):
            for j in range(padded.shape[1] - kernel_size + 1):
                subset = np.zeros((kernel_size, kernel_size))
                for a in range(kernel_size):
                    for b in range(kernel_size):
                        subset[a][b] = padded[i + a][j + b]
                convolved[i + k][j + k] = convolve(subset, kernel)
        new_convolved = np.zeros(original_shape, dtype = np.float32)
        for i in range(original_shape[0]):
            for j in range(original_shape[1]):
                new_convolved[i][j] = convolved[i + k][j + k]
    else:
        original_shape = (im.shape[0], im.shape[1], 3)
        padded = padImage(im, kernel_size, mode)
        k = (kernel_size - 1) // 2
        convolved = np.zeros((padded.shape[0], padded.shape[1], 3), dtype = np.float32)
        for i in range(padded.shape[0] - kernel_size + 1):
            for j in range(padded.shape[1] - kernel_size + 1):
                for channel in range(3):
                    subset = np.zeros((kernel_size, kernel_size))
                    for a in range(kernel_size):
                        for b in range(kernel_size):
                            subset[a][b] = padded[i + a][j + b][channel]
                    convolved[i + k][j + k][channel] = convolve(subset, kernel)
        new_convolved = np.zeros(original_shape, dtype = np.int32)
        for i in range(original_shape[0]):
            for j in range(original_shape[1]):
                for channel in range(3):
                    new_convolved[i][j][channel] = convolved[i + k][j + k][channel]
    return new_convolved

kernel_edge = np.asarray([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
kernel_sharpen = np.asarray([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel_gauss_blur =  np.asarray([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 256

im = mpimg.imread('test_image.jpg')
fig, axes = plt.subplots(2, 2)
fig.suptitle("Kernel Convolution Demo")
axes[0][0].imshow(im)
axes[0][0].set_title('Original Image')
axes[0][1].imshow(applyKernel(im, kernel_edge, mode = 1))
axes[0][1].set_title('Edge Detection')
axes[1][0].imshow(applyKernel(im, kernel_sharpen, mode = 1))
axes[1][0].set_title('Sharpened Image')
axes[1][1].imshow(applyKernel(im, kernel_gauss_blur, mode = 1))
axes[1][1].set_title('Gaussian Blurred Image')
plt.show()
