# 10. Dada una imagen cualquiera, generar su imagen en negativo. Recordar que para los valores
# RGB de un pixel cualquiera, el valor RGB del pixel en negativo será restarle a 255 ese
# pixel.

from PIL import Image as mg
import numpy as np 

imagen = mg.open('imagenes\ejer8.png')

pixeles = imagen.load()

for i in range(imagen.height):
    for j in range(imagen.width):
        r, g, b = imagen.getpixel((j, i))
        pixeles[j, i] = 255 - r, 255 - g, 255 - b

imagen.show()
