# 10. Implementar un programa que dada una imagen en escala de grises, genere una imagen
# suavizada (Blurring). Realice dos versiones, la primera con el filtro conocido como Box
# Filter de la figura 1 (promedio de los pixeles vecinos) y la segunda versión con el filtro
# Gaussiano de la figura 2. Compare sus resultados.

import cv2 as cv
import numpy as np

from Personal.funciones import *

kernel_1 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype='float')/9

kernel_2 = np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]], dtype='float')/16

imagen = cv.imread('imagenes\\spider.jpeg')

imagen_gris = promedio(imagen)

imagen_1 = convolucionar(imagen_gris, kernel_1) #BoxFilter

imagen_2 = convolucionar(imagen_gris, kernel_2) #Gaussiano

cv.imshow('Original', imagen)

cv.imshow('En Gris', imagen_gris)

cv.imshow('BoxFilter', imagen_1)

cv.imshow('Gaussiano', imagen_2)

cv.waitKey(0)

cv.destroyAllWindows()  

