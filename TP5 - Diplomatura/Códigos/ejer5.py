import numpy as np
import pandas as pd
from datetime import datetime
from Personal.funciones import *
import matplotlib.pyplot as plt

# Desnormalización de m y b  (min-max)
def desnormalizar_m_b(xs, ys, m_norm, b_norm):
    xs_min = np.min(xs)
    xs_max = np.max(xs)
    ys_min = np.min(ys)
    ys_max = np.max(ys)

    m_desnormal = (m_norm * (ys_max - ys_min)) / (xs_max - xs_min)
    b_desnormal = b_norm - \
        (m_norm * xs_min * (ys_max - ys_min)) / (xs_max - xs_min)

    return m_desnormal, b_desnormal

# Fecha a entero
def fecha_a_entero(fecha):
    return fecha.toordinal()


if __name__ == "__main__":
    datos = leer_datos_con_pandas('./fecha_dolar_bna.csv')

    if datos is None:
        print("No se pudo cargar el archivo.")
        exit(0)

    #Extración de datos
    xs = pd.to_datetime(datos['indice_tiempo'], format='%d/%m/%Y')
    xs_enteros = xs.apply(fecha_a_entero)
    xs_enteros = np.array([xs_enteros[i] for i in range(len(xs))])

    ys = [datos['tipo_cambio_bna_vendedor'][i]
                  for i in range(len(datos['tipo_cambio_bna_vendedor']))]

    # Normalización de los datos
    xs_normal = normalizar_datos(xs_enteros)
    ys_normal = normalizar_datos(ys)

    # Parámetros
    paso = 0.1
    tolerancia = 0.000000001

    # Descenso por el gradiente
    m, b = descenso_gradiente(xs_normal, ys_normal, paso, tolerancia)

    # Desnormalizar m y b, para graficar con
    # los datos originales
    m, b = desnormalizar_m_b(xs_enteros, ys, m, b)

    # Graficar
    fig, ax = plt.subplots(figsize=plt.figaspect(0.5)) #ancho = 2 * altura
    ax.plot(xs, ys, label="Muestras") #datos de entrenamiento
    ax.plot(xs, xs_enteros*m + b, label="Línea regresiva") #línea
    ax.set_xlabel("Fechas")
    ax.set_ylabel("Precios del dólar")
    ax.set_title("Precios del dólar oficial - BNA")
    ax.legend()
    plt.show()

    #Predicciones-> Noviembre 2023, Marzo de 2024 y Abril 2024
    fechas_txt = ['01/11/2023', '01/03/2024', '01/04/2024']
    fechas = pd.to_datetime(fechas_txt, format='%d/%m/%Y')
    fechas_enteros = [f.toordinal() for f in fechas]

    print("Predicciones para las siguientes fechas:")
    cadena = ""
    for i in range(len(fechas)):
        pred = (m*fechas_enteros[i] + b)
        print(fechas_txt[i], " -> $", round(pred, 2)) 
