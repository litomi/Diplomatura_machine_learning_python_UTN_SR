# 5. Idem que en el ejercicio 1, pero esta vez con la libreria Opencv_ Crear 3 imagenes
# de 600x800 pixeles, una roja, otra verde y otra amarilla. Guardarlas como rojo_cv.rgb,
# verde_cv.rgb y amarillo_cv.rgb

import cv2  as cv
import numpy as nP

marco = np.zeros((600, 800, 3), dtype= 'uint8')

marco[:] = 0, 0, 255 #BGR
cv.imwrite('imagenes/roja_cv.jpeg', marco)

marco[:] = 0, 255, 0 #BGR
cv.imwrite('imagenes/verde_cv.jpeg', marco)

marco[:] = 0, 233, 255 #BGR 
cv.imwrite('imagenes/amarilla_cv.jpeg', marco)

