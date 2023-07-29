# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:04:56 2022

@author: Lisandro
"""

# =============================================================================
# 5. Pedirle 8 números enteros al usuario y guardarlos en una lista. 
# Crear un array de una dimensión en base a dicha lista.
# =============================================================================
import numpy as np
import sys
nros = []

print("Ingrese 8 enteros.")
for i in range(8):
    while True:
        sys.stdout.flush() #limpia el buffer
        try:
            nros.append(int(input(("%d) ") % (i + 1))))
            break
        except:
            print("Sólo enteros.")

arreglo = np.array(nros)