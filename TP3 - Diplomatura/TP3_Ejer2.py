import cv2 as cv

import numpy as np

img = cv.imread('imagenes/cuadrado.jpg', 1)

img[np.where((img == [0, 0, 0]).all(axis = 2))] = [0, 255, 0]

cv.imshow('lero', img)

cv.imwrite('imagenes/cuadrado_a_verde.jpg', img)

cv.waitKey(0)
