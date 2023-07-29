import numpy as np
import random as rand
from Hopfield import *
from Imagen import *

if __name__ == "__main__":

    hopfield = Hopfield()
    imagen = Imagen()

    # Memorias
    # ps = [4, 8, 20]  # Cantidad de memorias almacenadas
    ps = [4, 8, 20]  # Cantidad de memorias almacenadas

    memorias = []

    # Imagen a reconocer
    imagen_a_reconocer = imagen.generar_imagen_binaria(10, 10)

    for p in ps:

        for _ in range(p):
            memorias.append(imagen.generar_imagen_binaria(10, 10).astype("int8"))

        # Imagen reconocida
        imagen_reconocida = hopfield.hopfield(memorias, imagen_a_reconocer)

        # Gráfica
        titulos = ["A reconocer", "reconocida"]

        imagenes = [imagen_a_reconocer, imagen_reconocida]

        imagen.mostrar_imagenes(imagenes, titulos, str(p) + " Memorias")
