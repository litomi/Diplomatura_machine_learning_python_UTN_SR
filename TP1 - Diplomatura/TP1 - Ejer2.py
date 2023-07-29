# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:33:22 2022

@author: Lisandro
"""

# =============================================================================
# 2.Implemente una función llamada dist, que tome 4 parámetros x1; y1; x2; y2 
# y devuelva la distancia entre los puntos (x1; y1) y (x2; y2). Utilicela para 
# corroborar las distancias entre los puntos del ejercicio anterior.
# =============================================================================

def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#a)(1, 7) y (5, 2)
print(("(%d, %d) -> (%d, %d) = %f") % (1, 7, 5, 2, dist(1, 7, 5, 2)))

#b)(1, 7) y (2, 7)
print(("(%d, %d) -> (%d, %d) = %f") % (1, 7, 2, 7, dist(1, 7, 2, 7)))

#c)(1, 7) y (1, 2)
print(("(%d, %d) -> (%d, %d) = %f") % (1, 7, 1, 2, dist(1, 7, 1, 2)))

#d)(-1, 7) y (-5, 2)
print(("(%d, %d) -> (%d, %d) = %f") % (-1, 7, -5, 2, dist(-1, 7, -5, 2)))

#e)(-1,-2) y (-3, 2)
print(("(%d, %d) -> (%d, %d) = %f") % (-1, -2, -3, 2, dist(-1, -2, -3, 2)))