# 15.Dada una imagen color cualquiera, mostrar en pantalla el siguiente collage de los 3 canales
# individuales de color de la misma.

from PIL import Image as mg
import numpy as np
from TP3_Ejer11_PILLOW import *

imagen = mg.open('imagenes\imagen_cualquiera_mediana.jpg')

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

img3 = np.concatenate((np.array(img1), np.array(img2), np.array(img3)), 1)

mg.fromarray(img3).show()