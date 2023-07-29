# 4. Implementar una función llamada bn que genere, a partir de una imagen y un valor
# llamado umbral una versión en blanco y negro de la misma. El valor de retorno de la
# función, sería la nueva imagen. Recuerde que la función de threshold, la más básica sería
# aquella que para un valor dado, si supera un umbral, devuelve el valor máximo, sino 0:
# * debería adaptarla a imagenes.

import cv2 as cv
from Personal.funciones import *

#-------------------------------------------------------------
imagen = cv.imread('imagenes\\ciudad.jpg')

imagen = luma(imagen)

imagen = bn(imagen, 200)

cv.imshow('img', imagen)
cv.waitKey(0)