import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Descenso gradiente, salida por los "cuadrados" 
# menor a tolerancia
def calcular_recta(xs, ys, paso, tolerancia):
    x_media = np.mean(xs)
    y_media = np.mean(ys)
    m = 0.0
    b = y_media - m * x_media #b inicial aproximado.

    while True:
        costo = calcular_costo(xs, ys, m, b)
        dm = derivada_m(xs, ys, m, b)
        db = derivada_b(xs, ys, m, b)
        m -= (paso * dm)
        b -= (paso * db)
        
        if abs(dm ** 2 + db ** 2) < tolerancia: break

    return m, b, costo

# Descenso gradiente, salida por la diferencia 
# de costos menor a tolerancia
def descenso_gradiente(xs, ys, paso, tolerancia):
    n = len(xs)
    m = 0
    b = 0
    costo_anterior = calcular_costo(xs, ys, m, b)

    while True:
        dm = derivada_m(xs, ys, m, b)  # derivada
        db = derivada_b(xs, ys, m, b)  # derivada
        m -= paso * dm
        b -= paso * db

        costo_actual = calcular_costo(xs, ys, m, b)

        if abs(costo_actual - costo_anterior) < tolerancia:
            break

        costo_anterior = costo_actual

    return m, b

def derivada_m(xs, ys, m, b):
    n = len(xs)
    derivada = (-2/n) * np.sum(xs * (ys - (m * xs + b)))
    return derivada

def derivada_b(xs, ys, m, b):
    n = len(xs)
    derivada = (-2/n) * np.sum(ys - (m * xs + b))
    return derivada

def calcular_costo(xs, ys, m, b):
    costo = np.mean((ys - (m * xs + b))**2)
    return costo

def graficar(xs, ys, m, b, xlabel ="", ylabel = ""):
    yes = m * xs + b
    plt.plot(xs, ys, 'o', color='blue', label='Datos')
    plt.plot(xs, yes, color='orange', label='Recta ajustada')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def imprimir_tabla_plot(dataframe: str):
    #figura y eje
    fig, ax = plt.subplots()

    #Tabla
    tabla = ax.table(cellText=dataframe.values,
                 colLabels=dataframe.columns, loc='center')

    # Estilos
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 1.2)

    ax.axis('off')
    plt.show()


"""
Leer los datos de un archivo tipo csv
utilizando Pandas
"""
def leer_datos_con_pandas(dir_archivo_csv: str):
    try:
        datos = pd.read_csv(dir_archivo_csv)
        return datos
    except:
        return None

def lineal(x, m, b):
    return x*m + b

# Normalización (min-max)
def normalizar_datos(datos):
    min = np.min(datos)
    max = np.max(datos)
    normales = (datos - min)/(max - min)
    return normales

#Normalización de datos fuera de las muestras
def normalizar_según_datos(datos, nor):
    min = np.min(datos)
    max = np.max(datos)
    normales = (nor - min)/(max - min)
    return normales

# Desnormalización (min-max)
def desnormalizar_datos(datos, datos_normalizados):
    min = np.min(datos)
    max = np.max(datos)
    desnormales = datos_normalizados*(max - min) + min
    return desnormales


#Normalización por estandararización
def estandarizacion_datos(datos):
    media = np.mean(datos)
    std = np.std(datos)
    datos_estandarizados = (datos - media) / std
    return datos_estandarizados


# Convertir la fecha a un entero
def fecha_a_entero(fecha, separador):
    fecha = fecha.replace(separador, "")[:8]
    return int(fecha[:4]) * 365 + int(fecha[:2]) + int(fecha[3:5])