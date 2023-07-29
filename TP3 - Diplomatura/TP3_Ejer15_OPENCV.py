# 15.Dada una imagen color cualquiera, mostrar en pantalla el siguiente collage de los 3 canales
# individuales de color de la misma.

import cv2 as cv
from TP3_Ejer11_OPENCV import *

imagen = cv.imread('imagenes\imagen_cualquiera_mediana.jpg', 1)

img1 = imagen.copy()
img2 = imagen.copy()
img3 = imagen.copy()

#rojo
quitar_azul(img1)
quitar_verde(img1)

#verde
quitar_azul(img2)
quitar_rojo(img2)

#azul
quitar_rojo(img3)
quitar_verde(img3)

img = cv.hconcat([img1, img2, img3])

cv.imwrite('imagenes\img_concatenadas.jpg', img)

cv.imshow('', img)

cv.waitKey(0)

cv.destroyAllWindows()


