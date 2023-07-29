from Personal.funciones import estandarizacion_datos, leer_datos_con_pandas
import numpy as np


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

def predecir(x, pesos, b):
    return np.dot(x, pesos) + b


if __name__ == "__main__":
    #Lectura de los datos
    datos = leer_datos_con_pandas("./celulares_train.csv")

    if datos is None:
        print("ERROR: No se pudo cargar el archivo")
        exit(0)

    # Columnas seleccionadas -variables-
    columnas = ['bateria', 'camara_frontal',
                'altura_pixeles', 'ancho_pixeles', 'RAM']

    # Variables
    xss = np.array(datos.loc[:, columnas], dtype="float64")

    # Valores a predecir
    ys = np.array(datos['rango_precio'], dtype="float64")

    # Normalización
    xss = estandarizacion_datos(xss)

    # Parámetros
    taza_aprendizaje = 0.01
    iteraciones = 1000

    #Descenso por el gradiente
    pesos, b, costos = descenso_gradiente(
        xss, ys, taza_aprendizaje, iteraciones)

    #Datos de prueba
    data = np.array([
        [1043, 14, 226, 1412, 3476],
        [841, 4, 746, 857, 3895],
        [1807, 1, 1270, 1366, 2396],
        [1546, 18, 295, 1752, 3893],
        [1434, 11, 749, 810, 1773],
        [1464, 5, 569, 939, 3506],
        [1718, 1, 1283, 1374, 3873],
        [833, 0, 1312, 1880, 1495]
    ], dtype="int32")

    # Normalización de los datos de prueba
    data_normal = estandarizacion_datos(data)

    print("------------------------------------------------------------------------------------------")   
    c = columnas
    print(f"{c[0]:>10} {c[1]:>15} {c[2]:>15} {c[3]:>15} {c[4]:>6} {'Rango':>10}".upper())
    for i in range(len(data)):
        print(f"{data[i][0]:10d} {data[i][1]:15d} {data[i][2]:15d} {data[i][3]:15d} {data[i][4]:6d}", end=" ==> ")
        print(f"{round(predecir(data_normal[i], pesos, b)):>6}")
    print("------------------------------------------------------------------------------------------")   

    
