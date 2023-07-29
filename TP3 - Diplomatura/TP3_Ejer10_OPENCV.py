# 10. Dada una imagen cualquiera, generar su imagen en negativo. Recordar que para los valores
# RGB de un pixel cualquiera, el valor RGB del pixel en negativo será restarle a 255 ese
# pixel.

import cv2 as cv
import numpy as np 

imagen = cv.imread('imagenes\imagen_cualquiera.jpg', 1)

for i in range(len(imagen)):
    for j in range(len(imagen[i])):
        a, b, c = imagen[i][j]
        imagen[i][j] = 255 - a, 255 - b, 255 - c

cv.imwrite('imagenes\imagen_cualquiera_invertida.jpg', imagen)

cv.imshow('', imagen)

cv.waitKey(0)

cv.destroyAllWindows()
