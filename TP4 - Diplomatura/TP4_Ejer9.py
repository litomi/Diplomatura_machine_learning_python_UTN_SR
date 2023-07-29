# 9. Dada la imagen original actor.png en color, generar la siguiente imagen, ¿Qué pasos
# debería hacer para lograrlo?

# Pasos:
# -Abrir la imagen y guardar
# -Convertir los colores a grises
# -Procesar la imagen en forma binaria
#    -Recorrer cada pixel
#       -Si pixel > umbral:
#           -pixel <- 180
#       -Sino:
#          -pixel <- 0
# -Concatenar las imágenes
#

import cv2 as cv
from Personal.funciones import *
import matplotlib.pyplot as plt
import numpy as np

imagen = cv.imread('imagenes\\actor.png')

imagen_binaria = bn_gris_3_canales(luma_tres_valores(imagen), 110)

img = cv.hconcat([imagen, imagen_binaria])

cv.imshow('actor.png', img)

cv.waitKey(0)

cv.destroyAllWindows()
