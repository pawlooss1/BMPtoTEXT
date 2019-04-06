#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import os


# In[83]:


def decode_n_bytes(image, n):
    word = image.read(n)
    return int.from_bytes(word, byteorder='little')


# In[93]:


def image_to_array(file_name):
    image = open('ludzie.bmp', 'rb')
    trash = image.read(2)
    size = decode_n_bytes(image, 4)
    trash = image.read(4)
    offset = decode_n_bytes(image, 4)
    trash = image.read(4)
    width = decode_n_bytes(image, 4)
    height = decode_n_bytes(image, 4)
    trash = image.read(2)
    bpp = decode_n_bytes(image, 2)
    bytes_per_pixel = bpp // 8
    image = open('ludzie.bmp', 'rb')
    trash = image.read(offset)
    array = np.empty((height, width), dtype = int)
    for i in range(height):
        for j in range(width):
            byte = image.read(1)
            number = int.from_bytes(byte, byteorder='big')
            array[height-1-i][j] = number
            image.read(bytes_per_pixel - 1)
    return array

