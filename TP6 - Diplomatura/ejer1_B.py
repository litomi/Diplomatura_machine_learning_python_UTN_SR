import numpy as np
import random as rand
from Hopfield import *
from Imagen import *

if __name__ == "__main__":

    hopfield = Hopfield()
    imagen = Imagen()

    # Memorias
    memorias = []
    for _ in range(2):
        memorias.append(imagen.generar_imagen_binaria(10, 10).astype("int8"))
    
    # Imagen a reconocer
    imagen_a_reconocer = imagen.generar_imagen_binaria(10, 10)

    # Imagen reconocida
    imagen_reconocida = hopfield.hopfield(memorias, imagen_a_reconocer)

    # Gráfica
    titulos = ["Memoria 1", "Memoria 2",
               "Imagen a reconocer", "Imagen reconocida"]
    imagenes = memorias + [imagen_a_reconocer, imagen_reconocida]

    imagen.mostrar_imagenes(imagenes, titulos, "2 memorias")
