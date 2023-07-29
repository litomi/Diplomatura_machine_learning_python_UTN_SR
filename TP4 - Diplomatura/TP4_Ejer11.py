# 11. Implementar un programa que dada una imagen en escala de grises (o en color, pero
# convertida a grises) aumente su nitidez, utilizando alguno de los kernel de Laplace dados
# a continuación. (Sharpen)

import cv2 as cv
import numpy as np

from Personal.funciones import *

laplace_1 = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype='float')

laplace_2 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype='float')

imagen = cv.imread('imagenes\\perrito.jpg')

imagen_gris = luma(imagen)


imagen_1 = convolucionar(imagen_gris, laplace_1)

imagen_2 = convolucionar(imagen_gris, laplace_2)

cv.imshow('Original', imagen)

cv.imshow('Original en gris', imagen_gris)

cv.imshow('Laplace kernel 1', imagen_1)

cv.imshow('Laplace kernel 2', imagen_2)

cv.waitKey(0)

cv.destroyAllWindows()




