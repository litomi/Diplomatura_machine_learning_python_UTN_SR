# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:34:23 2022

@author: Lisandro
"""

# =============================================================================
# 3.Para cada par de puntos dados en el ejercicio anterior, obtenga la recta
# que pasa por ellos. Implemente además, una función llamada recta que
# dadas las coordenadas de dos puntos, devuelva la pendiente y la ordenada 
# al origen de la función que pasa por ellos. Devolverá ambos valores en 
# una tupla del estilo (m, b).
# =============================================================================
# a)(1, 7) y (5, 2)
# y = -5/4x + 33/4
 
 
# b)(1, 7) y (2, 7)
# y = 7

# c)(1, 7) y (1, 2)
# x = 1

# d)(-1, 7) y (-5, 2)
# y = 5/4x + 33/4

# e)(-1,-2) y (-3, 2)
# y = -2x - 4

# y - y1 = (y2 - y1 / x2 -x1) (x - x1)
def recta(x1, y1, x2, y2):
    if (x2 - x1) != 0:
        return  ((y2 - y1) / (x2 - x1), ((y2 - y1) / (x2 - x1)) * -x1 + y1)
    return ("Indeterminado", x1)