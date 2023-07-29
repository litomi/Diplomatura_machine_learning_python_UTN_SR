# 11. Implementar 3 funciones, cada una se encargará de eliminar uno de los tonos de una imagen
# cualquiera. Las funciones llamadas quitar rojo, quitar azul y quitar verde tomarán
# un solo parámetro, la imagen.

from PIL import Image as mg 

def quitar_rojo(imagen):
    matriz = imagen.load()
    for i in range(imagen.height):
        for j in range(imagen.width):
            r, g, b = imagen.getpixel((j, i))
            matriz[j, i] = (0, g, b)

def quitar_verde(imagen):
    matriz = imagen.load()
    for i in range(imagen.height):
        for j in range(imagen.width):
            r, g, b = imagen.getpixel((j, i))
            matriz[j, i] = (r, 0, b)

def quitar_azul(imagen):
    matriz = imagen.load()
    for i in range(imagen.height):
        for j in range(imagen.width):
            r, g, b = imagen.getpixel((j, i))
            matriz[j, i] = (r, g, 0)
