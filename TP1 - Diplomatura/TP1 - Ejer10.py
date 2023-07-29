# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:02:02 2022

@author: Lisandro
"""

# =============================================================================
# 10. Grafique la función tangente hiperbólica en el intervalo [-5, 10]. (Se 
# llama tanh, y la tiene en varias librerías, math, numpy)
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(-5, 10)


fig = plt.figure() 
fig.set_size_inches(8, 5)

plt.grid()
plt.plot(x, np.tanh(x), label = "f(x) = tanh(x)")
plt.legend(loc=4)
plt.show()