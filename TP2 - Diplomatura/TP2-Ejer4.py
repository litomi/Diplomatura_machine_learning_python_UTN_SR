# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:51:52 2022

@author: Lisandro
"""

# =============================================================================
# 4. Supongamos tienes una lista con las alturas en cm de todos los miembros de 
# tu familia, # por ejemplo [181.5, 72., 34.7, 171.3, 160.1]. Crear un array y 
# mostrar sus atributos, el tipo de datos, tanto del array como de sus elementos.
# Mostrar también el total de familiares cargados en el array
# =============================================================================
import numpy as np
alturas = np.array([181.5, 72.8, 34.7, 171.3, 160.1])

print("Un objeto de búfer de Python que apunta a la posición inicial de los datos: "
      , alturas.data)
print("Número de elementos:", alturas.size)
print("El tamaño de cada elemento en bytes:", alturas.itemsize)
print("La memoria total (en bytes) ocupada:", alturas.nbytes)
print("El número de dimensiones contenidas :", alturas.ndim)
print("El tipo de datos del elemento contenido:", alturas.dtype)
print("Parte real de los datos:", alturas.real)
print("La parte imaginaria de los datos:", alturas.imag)
print("El objeto en el que se basa:", alturas.base)
print("Información sobre cómo almacenar los datos:", alturas.flags)
print("Un iterador que convierte a Ndarray en un array unidimensional: ", alturas.flat)

print("TOTAL DE FAMILIARES CARGADOS:", alturas.size)

