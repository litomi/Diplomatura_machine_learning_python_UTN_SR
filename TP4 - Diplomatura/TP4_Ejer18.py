# 18. Crear una función llamada flip que tome dos parámetros: una imagen y un eje (eje sería
# una variable del tipo str, que contendría uno de dos valores posibles, horizontal o vertical)
# Devolver una nueva imagen que sea la versión espejada de la imagen original, sobre el eje
# vertical o sobre el eje horizontal según corresponda.

import cv2 as cv
import numpy as np
from Personal.funciones import flip

imagen = cv.imread('imagenes\\actriz.png')

img_inversion_horizontal = flip(imagen, 'horizontal')

img_inversion_vertical = flip(imagen, 'vertical')

cv.imshow('Original', imagen)

cv.imshow('Horizontal', img_inversion_horizontal)

cv.imshow('Vertical', img_inversion_vertical)

cv.waitKey(0)

cv.destroyAllWindows()