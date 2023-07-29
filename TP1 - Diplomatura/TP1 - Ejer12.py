# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:39:14 2022

@author: Lisandro
"""

# =============================================================================
# 12.Genere un archivo de texto con valores aleatorios entre -2.00 y 2.98 
# en una primer columna, separados por coma, de una segunda columna que
# contenga valores aleatorios entre 0.0 a 0.99. Debería haber unas 1000 
# filas de datos en el archivo. Grafique los datos en el intervalo [0, 2]
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import random as ran

archivo = open("valores_aletorios.txt", "w+")
for i in range(1001):
    archivo.write(
        ("%.2f,%.2f\n") % (ran.uniform(-2.00, 2.98), ran.uniform(0.00, 0.99))
    )
archivo.close()

archivo = open("valores_aletorios.txt", "r")
lineas = archivo.readlines()
archivo.close()

#colecta de los datos
c1 = []
c2 = []
for l in lineas:
    a, b = l.strip().split(",")
    c1.append(float(a))
    c2.append(float(b))

x = np.linspace(0, 2, len(c1))
fig = plt.figure() 
fig.set_size_inches(15, 9)
                    
plt.plot(x, c1, "ob-", label= "Columna 1")
plt.plot(x, c2, "or-", label= "Columna 2")
plt.grid()
plt.legend(loc=0)
plt.show()
