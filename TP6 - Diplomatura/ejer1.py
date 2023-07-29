import numpy as np
from Hopfield import *
from Imagen import *

if __name__ == "__main__":

    imagen_binaria = np.array([
        [ 1,  1,  1,  1, -1, -1,  1,  1,  1,  1],
        [ 1,  1,  1, -1, -1,  1,  1,  1, -1,  1],
        [-1, -1, -1,  1, -1, -1, -1, -1,  1,  1],
        [ 1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
        [-1,  1,  1, -1, -1, -1,  1, -1, -1,  1],
        [ 1,  1, -1, -1,  1,  1, -1, -1, -1, -1],
        [ 1,  1,  1, -1,  1, -1,  1, -1,  1, -1],
        [-1,  1,  1,  1,  1, -1, -1,  1, -1, -1],
        [ 1,  1, -1, -1,  1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1,  1,  1, -1, -1, -1]
    ])

    imagen_a_reconocer = np.array([
        [ 1,  1,  1,  1,  1, -1,  1,  1,  1,  1],
        [ 1,  1,  1, -1,  1,  1,  1,  1, -1,  1],
        [-1, -1, -1,  1, -1, -1, -1, -1,  1,  1],
        [ 1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
        [ 1,  1,  1,  1, -1, -1,  1,  1, -1,  1],
        [ 1,  1,  1, -1,  1,  1, -1, -1, -1,  1],
        [ 1,  1,  1, -1,  1,  1,  1, -1,  1, -1],
        [-1,  1,  1,  1,  1,  1,  1,  1, -1,  1],
        [ 1,  1, -1,  1,  1, -1, -1, -1,  1, -1],
        [-1, -1,  1, -1,  1,  1,  1, -1, -1, -1],
    ])    

    hopfield = Hopfield()
    imagen = Imagen()

    #Prueba con las matrices dadas en el práctico
    imagen_reconocida = hopfield.hopfield([imagen_binaria], imagen_a_reconocer)

    #Graficando
    titulos = ["Memoria", "Imagen a reconocer", "Imagen reconocida"]
    imagenes = [imagen_binaria, imagen_a_reconocer, imagen_reconocida]
    imagen.mostrar_imagenes(imagenes, titulos, "Imágenes de prueba")


