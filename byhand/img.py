# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def img_array():

    imgs = np.load('x_all.npy')
    return imgs


def check_image():

    imgs = img_array()

    plt.imshow(imgs[0], cmap='gray')
    plt.show()


def get_shape():

    imgs = img_array()
    print(imgs.shape)


if __name__ == '__main__':
    get_shape()
