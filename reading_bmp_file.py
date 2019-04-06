import numpy as np
import os

def decode_n_bytes(image, n):
    word = image.read(n)
    return int.from_bytes(word, byteorder='little')

def get_metadata(file_name):
    image = open(file_name, 'rb')
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
    return (size, offset, width, height, bytes_per_pixel)

def image_to_array(file_name):
    meta = get_metadata(file_name)
    offset = meta[1]
    width = meta[2]
    height = meta[3]
    bpp = meta[4]
    if (width * bpp) % 4 == 0:
        fill_to_4 = 0
    else:
        fill_to_4 = 4 - (width * bpp) % 4
    image = open(file_name, 'rb')
    trash = image.read(offset)
    array = np.empty((height, width * 2), dtype = int)
    for i in range(height):
        for j in range(0, width * 2, 2):
            sum = 0
            for k in range(bpp):
                byte = image.read(1)
                sum = sum + int.from_bytes(byte, byteorder='big')            
            mean = sum / bpp
            array[height-1-i][j] = mean
            array[height-1-i][j+1] = mean
        if fill_to_4 > 0:
            trash = image.read(fill_to_4)
    return array
