from Personal.funciones import *

if __name__ == "__main__":
    datos = leer_datos_con_pandas("./notas_horasestudio.csv")

    if datos is None:
        print("ERROR: No se pudo cargar el archivo")
        exit(0)

    # Datos
    xs = np.array(datos['Horas'])
    ys = np.array(datos['Notas'])

    # Optimización
    paso = 0.001
    tolerancia = 0.000001

    # Calcular
    m, b, costo = calcular_recta(xs, ys, paso, tolerancia)

    # Graficar
    graficar(xs, ys, m, b, "Horas", "Notas")

    # Ejemplo de aplicación
    for h in range(11):
        nota = lineal(h, m, b) 
        print("Horas estudias: %2d -> nota: %2.2f" %
              (h, 100.00 if nota > 100.00 else nota))
