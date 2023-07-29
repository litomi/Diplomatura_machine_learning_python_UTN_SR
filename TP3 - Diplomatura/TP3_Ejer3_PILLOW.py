# 3.Crear una imagen del tamañoo que desee, que tenga un arcoiris de 6 colores, organizada
# en 6 grandes rayas horizontales.

from PIL import Image as img
import math
import numpy as np

#procedimiento
def dibujarFranjas(pixeles, ancho, alto, colores):
    c = -1
    while (c := c + 1) < len(colores):
        tramo = math.ceil(alto / len(colores))
        min = tramo * c
        max = min + tramo
        max = max if max < alto else alto #corrección de desborde

        for i in range(min, max): #alto
            for j in range(ancho): #ancho
                pixeles[i][j] = colores[c]

colores = (
    (211, 0, 148),
    (130, 0, 75),
    (255, 0, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 127, 255)
)

imagen = img.new('RGB', (800, 400), 'white')

pixeles = np.array(imagen)

ancho, alto = imagen.size

dibujarFranjas(pixeles, ancho, alto, colores)

imagen = img.fromarray(pixeles)

imagen.show()