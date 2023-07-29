# 15. Implemente un programa que permita ingresar una imagen, y detecte los bordes de la
# misma, realice las siguientes versiones:
# a)Detección de Bordes de Laplace.
# b)Detección de Bordes de Sobel, sin suavizar.
# c)Detección de Bordes de Sobel, con previo suavizado.

import cv2 as cv
import numpy as np

from Personal.funciones import *

laplace = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
], dtype='float')

sobel_h = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
], dtype='float')

sobel_v = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype='float')

kernel_gauss = np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]
], dtype='float') / 256

imagen = cv.imread('imagenes\\spider.jpeg')
imagen_gris = luma(imagen)

# a)
imagen_laplace = convolucionar(imagen_gris, laplace)

# b)
imagen_sobel = convolucionar(imagen_gris, sobel_h) #horizontal
imagen_sobel = convolucionar(imagen_sobel, sobel_v) #vertical

# c)
imagen_suavizada = convolucionar(imagen_gris, kernel_gauss)
imagen_sobel_suavizado = convolucionar(imagen_suavizada, sobel_h) #horizontal
imagen_sobel_suavizado = convolucionar(imagen_sobel_suavizado, sobel_v) #vertical

cv.imshow('Original', imagen)
cv.imshow('En gris', imagen_gris)
cv.imshow('Laplace', imagen_laplace)
cv.imshow('Sobel - sin suavizar', imagen_sobel)
cv.imshow('imagen suavizada', imagen_suavizada)
cv.imshow('Sobel - suavizada', imagen_sobel_suavizado)

cv.waitKey(0)

cv.destroyAllWindows()    