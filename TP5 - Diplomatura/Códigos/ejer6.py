import numpy as np
import matplotlib.pyplot as plt


def descenso_gradiente(xss, y, aprendizaje, iteraciones):
    num_datos, num_variables = xss.shape

    # parámetros
    pesos = np.zeros(num_variables)
    b = 0
    costos = []

    for vuelta in range(iteraciones):
        # Costo
        y_pred = np.dot(xss, pesos) + b
        costos.append(np.mean((y_pred - y) ** 2))  # guardado de costo

        # Cálculo del gradiente
        gradiente_pesos = (2/num_datos) * np.dot(xss.T, (y_pred - y))
        gradiente_b = (2/num_datos) * np.sum(y_pred - y)

        # Actualización
        pesos -= aprendizaje * gradiente_pesos
        b -= aprendizaje * gradiente_b

    return pesos, b, costos


def graficar_costos(costos, xlabel="", ylabel="", title=""):
    plt.plot(costos, color='blue', label='Costos')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    xss = np.array([[1, 1, 1], [1, 3, 4], [3, 4, 5], [2, 2, 2], [3, 3, 3], [
                   0, 1, 1]])  # Datos de entrada
    ys = np.array([10, 28, 39, 19, 28, 8])  # Objetivo

    #Parámetros
    taza_aprendizaje = 0.01
    iteraciones = [10, 100, 1000, 10000]

    #Graficas
    fig, axes = plt.subplots(2, 2, figsize = (10, 5))

    fig.suptitle("Gráficas de costos.")

    for ax, i in zip(axes.flat, iteraciones):
        pesos, b, costos = descenso_gradiente(xss, ys, taza_aprendizaje, i)
        print("---------------------------")
        print("Iteraciones: ", i)
        print("Coeficientes->", end=" ")
        print("m1:", round(pesos[0]), "m2:", round(pesos[1]), "m3:", round(pesos[2]))
        print("Ordenada-> b:", round(b))
        #gráfica
        ax.set_title(f'Iteraciones: {i}', fontsize='medium')
        ax.plot(costos)

    plt.tight_layout(pad=0.5, w_pad=4, h_pad=1)
    plt.show()

