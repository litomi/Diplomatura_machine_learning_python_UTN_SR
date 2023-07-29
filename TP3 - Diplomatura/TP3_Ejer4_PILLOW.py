# 4. Implementar una función llamada saturar que tome dos parámetros, la imagen a saturar
# y el porcentaje que se desea de saturación. Convirtiendo de RGB al espacio de color HSV.
# (Hue, Saturation, Value = Tono/Matiz, Saturación, Brillo/Valor)
# *Ayuda: Una vez abierta la imagen, utilice el comando de Pillow imagen.convert('HSV')
# para realizar la conversión del espacio de color)

from PIL import Image, ImageColor
import numpy as np

imagen = Image.open('imagenes/cuadrado.jpg').convert(mode="HSV")

def saturar(imagen, sat):
    pixeles = imagen.load()
    alto, ancho = imagen.size

    s =  255 * sat/100
    s = s if s < 255 else 255
    
    for i in range(alto):
        for j in range(ancho):
            a, b, c = pixeles[i, j]
            pixeles[i, j] = (a, int(s), c)

saturar(imagen, 50)

imagen.show()