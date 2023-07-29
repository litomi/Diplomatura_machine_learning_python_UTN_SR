# 8. Dada la imagen adjuntada en el práctico, llamada puros.jpg realizar un programita que
# transforme el triángulo rojo a un triáangulo amarillo. Observar que se tiene una imagen
# con colores planos puros.

import cv2 as cv
import numpy as np

imagen = cv.imread('imagenes\puros.png', 1)

imagen[np.where((imagen == [0, 0, 255]).all(axis = 2))] = [0, 255, 255]

cv.imwrite('imagenes\ejer8.png', imagen)

cv.imshow('', imagen)

cv.waitKey(0)

cv.destroyAllWindows()