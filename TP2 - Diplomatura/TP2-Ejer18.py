# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 05:14:34 2022

@author: Lisandro
"""

# =============================================================================
# 18.Implemente una función prod_punto que tome dos vectores y devuelva el
# producto escalar de ambos. ¿Funciona igual con listas que con arrays? 
# ¿Necesitaría realizar dos implementaciones distintas?
# Respuesta: Funciona igual, no se necesitan dos implementaciones diferentes.
# =============================================================================
import numpy as np
import random as ran
#Listas
l1 = [ ran.randint(-100, 100) for x in range(100)]
l2 = [ ran.randint(-100, 100) for x in range(100)]

#Arreglos
m1 = np.array(l1)
m2 = np.array(l2)

#artesanal
def prod_punto(v1, v2):
    if len(v1) == len(v2):
        res = 0
        for i in range(len(v1)):
            res += v1[i] * v2[i]
        return res
    return

print("----Artesanal----")
print("Listas: ", prod_punto(l1, l2))
print("Arreglos: ", prod_punto(m1, m2))

#numpy
def prod_punto_numpy(v1, v2):
    return np.dot(v1, v2)

print("----Numpy----")
print("Listas: ", prod_punto_numpy(l1, l2))
print("Arreglos: ", prod_punto_numpy(m1, m2))