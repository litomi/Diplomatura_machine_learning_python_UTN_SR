import matplotlib.pyplot as plt
import random as rand
import numpy as np

class Imagen:
    def __init__(self):
        pass

    # Muestra las imágenes en un gráfico con su respectivo nombre
    def mostrar_imagenes(self, imagenes:list, titulos:list, titulo:str):
        fig, axs = plt.subplots(1, len(imagenes), figsize=(10, 10))
        for i in range(len(imagenes)):
            axs[i].imshow(imagenes[i], cmap="gray")
            axs[i].set_title("{}".format(titulos[i]))
        fig.suptitle(titulo)
        fig.set_figheight(4)
        plt.show()
    
    # Genera imagen binaria como matriz de Numpy
    def generar_imagen_binaria(self, ancho, alto):
        return np.array([[rand.choice([-1, 1]) for _ in range(ancho)] for _ in range(alto)])

    # Cambia n píxeles aleatoriamente 
    def cambiar_pixeles(self, matriz, n:int):
        m = matriz.flatten()
        indices = rand.sample(range(len(m)), n)
        for i in indices: m[i] *= -1
        return m.reshape(matriz.shape)