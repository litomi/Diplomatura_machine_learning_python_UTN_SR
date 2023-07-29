# 13. Implemente ahora un programa que aplique el filtro Gaussiano de 5x5. ¿Encuentra diferencias
# con la versión de 3x3?

import cv2 as cv
import numpy as np

from Personal.funciones import *

gaussiano = np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]   
    ], dtype= 'float') / 273

imagen = cv.imread('imagenes\\spider.jpeg')

imagen_gris = luma(imagen)

imagen_1 = convolucionar(imagen_gris, gaussiano)

cv.imshow('original', imagen)

cv.imshow('original en grises', imagen_gris)

cv.imshow('Gaussiano 5x5', imagen_1)

cv.waitKey(0)

cv.destroyAllWindows()
