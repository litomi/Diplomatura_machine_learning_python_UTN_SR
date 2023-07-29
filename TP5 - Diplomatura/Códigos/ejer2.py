from Personal.funciones import *
import pandas as pd
import numpy as np


if __name__ == "__main__":

    dir_archivo_csv = "./heights_weights.csv"
    datos = leer_datos_con_pandas(dir_archivo_csv)

    if datos is None:
        print("ERROR: El archivo no existe.")
        exit(0)

    #Tabla en ventana
    imprimir_tabla_plot(datos)

    #Datos para calcular y graficar
    xs = np.array(datos['Height'])  # altura
    ys = np.array(datos['Weight'])  # peso

    # Optimización
    paso = 0.01
    tolerancia = 0.0001

    # Calcular
    m, b, costo = calcular_recta(xs, ys, paso, tolerancia)

    # Graficar
    graficar(xs, ys, m, b, "Alturas(m)", "Pesos(kg)")

    #Consola
    print("Estimaciones:")
    print("Mujer de %2.2f m de altura peso estimado en %2.2f kg" % (1.30, lineal(1.30, m, b)))
    print("Mujer de %2.2f m de altura peso estimado en %2.2f kg" % (1.60, lineal(1.60, m, b)))
    print("Mujer de %2.2f m de altura peso estimado en %2.2f kg" % (2.00, lineal(2.00, m, b)))


