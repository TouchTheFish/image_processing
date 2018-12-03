# -*- coding: UTF-8 -*-
import numpy as np
from PIL import Image


def impulse_noise(img, ratio):
    """

    :param img: 原图像
    :param ratio: 胡椒噪的比例
    :return:
    """
    data = np.array(img)

    rows, cols, dims = data.shape
    salt_num = int(ratio * rows * cols)
    for i in range(salt_num):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        data[x, y, 0:1] = 255
    for i in range(salt_num):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        data[x, y, 1:2] = 255
    for i in range(salt_num):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        data[x, y, 2:3] = 255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im
