# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:00:28 2022

@author: Lisandro
"""
# =============================================================================
# 9.Implemente la función escalón y grafiquela en el intervalo [-5, 5]. 
# =============================================================================


import matplotlib.pyplot as plt
import numpy as np

def escalon(n):
    return 0 if n < 0 else 1

x1 = [x for x in np.arange(-5, 0, .1)]
x2 = [x for x in np.arange(0, 5 + .1, .1)]
y1 = [escalon(y) for y in x1]
y2 = [escalon(y) for y in x2]


fig = plt.figure() 
fig.set_size_inches(10, 5)

plt.axis("equal")
plt.grid()
plt.plot(x1, y1, "g")
plt.plot(x2, y2, "g")
plt.legend(["Función escalón."])

plt.show()