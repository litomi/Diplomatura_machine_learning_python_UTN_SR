import numpy as np

class Hopfield:
    def __init__(self):
        pass

    # imagen: Los patrones de entrenamiento como una matriz de NumPy.
    # retorna: La matriz de pesos de la red neuronal.
    def obtener_pesos(self, imagenes: list):
        n = imagenes[0].shape[0] * imagenes[0].shape[0]
        pesos = np.zeros((n, n))
        for img in imagenes:
            img_plana = img.flatten()
            pesos += img_plana * \
                img_plana.reshape(len(img_plana), 1) - \
                np.eye(len(img_plana), dtype="int8")
        return pesos

    # Función de activación
    # Matriz: La matriz sobre aplicaa la función
    def activacion(self, matriz):
        activada = np.zeros(matriz.shape)
        matriz = matriz.astype("int8")
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                activada[i][j] = 1 if matriz[i][j] > 0 else -1
        return activada

    # Multiplicación de matrices
    def mult_matrices(self, m1, m2):
        return m1.dot(m2)

    def hopfield(self, memorias: list, imagen_a_reconocer):

        dim = memorias[0].shape

        # Se obtiene la matriz de pesos
        pesos = self.obtener_pesos(memorias)

        # Multiplicación por la matriz de pesos
        imagen_temp = self.mult_matrices(imagen_a_reconocer.flatten(), pesos)

        # Retomando las dimensiones
        imagen_temp = imagen_temp.reshape(dim)

        # Función activación
        imagen_reconocida = self.activacion(imagen_temp)

        # Multiplicación por la matriz de pesos
        imagen_reconocida = self.mult_matrices(imagen_reconocida.flatten(), pesos)

        # Función activación
        imagen_reconocida = self.activacion(imagen_reconocida.reshape(dim))

        # Retomando las dimensiones y devolviendo la imagen reconocida.
        return imagen_reconocida.reshape(dim)


