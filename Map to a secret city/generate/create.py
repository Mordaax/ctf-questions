import numpy as np
import cv2
import random


def generate():
    img = cv2.imread('original.png', 1)
    f = open('map.txt', 'a')
    for y in range(len(img)):
        for x in range(len(img[0])):
            if np.array_equal([0, 0, 0], img[y][x]):
                f.write(hex(y) + ' ' + hex(x) + "\n")


generate()
lines = open('map.txt').readlines()
random.shuffle(lines)
open('map.txt', 'w').writelines(lines)
