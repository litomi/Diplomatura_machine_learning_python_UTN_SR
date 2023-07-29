import numpy as np
import random as rand
from Hopfield import *
from Imagen import *

if __name__ == "__main__":

    hopfield = Hopfield()
    imagen = Imagen()
    cambios = [10, 3, 50]

    #Memoria
    imagen_binaria = imagen.generar_imagen_binaria(10, 10)

    for pixeles in cambios:
        

        #Imagen a reconocer
        imagen_a_reconocer = imagen.cambiar_pixeles(imagen_binaria, pixeles)

        #Imagen reconocida
        imagen_reconocida = hopfield.hopfield([imagen_binaria], imagen_a_reconocer)

        #Gráfica
        titulos = ["Memoria", "Imagen a reconocer", "Imagen reconocida"]
        imagenes = [imagen_binaria, imagen_a_reconocer, imagen_reconocida]

        imagen.mostrar_imagenes(imagenes, titulos, str(pixeles) + " píxeles cambiados")
    




