# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:05:14 2022

@author: Lisandro
"""

# =============================================================================
# 6.Sea f(x) = 5x^5 - x^4 +3x^3 + x^2 - 2x - 8
# Halle la pendiente de la función f(x) en 
#     a = 3,
#     a = 4,
#     a = 5,
#     a = 5.1,
#     a = 5.2,
#     a = 5.3,
#     a = 5.4 
# y grafique esos puntos *(x versus las pendientes estimadas)
# =============================================================================
import matplotlib.pyplot as plt

def pendiente(x, y, h):
    return ((y + h) - y) / ((x + h) - x)

def ordenada(x):
    return 5*pow(x, 5) - pow(x, 4) + 3*pow(x, 3) + pow(x, 2) -2*x - 8

x = [3, 4, 5, 5.1, 5.2, 5.3, 5.4]
y = [pendiente(n, ordenada(n), 0.00000000001) for n in x]


fig = plt.figure() 
fig.set_figheight(10)
fig.set_figwidth(10)

plt.plot(x, y, "o--")
plt.show()


