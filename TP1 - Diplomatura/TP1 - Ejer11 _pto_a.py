# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:06:13 2022

@author: Lisandro
"""

# =============================================================================
# 11.Grafique
# a) f(x) = x^2 x en [-8, 8]
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-8, 8)

fig = plt.figure() 
fig.set_size_inches(8, 5)

plt.plot(x, x**2)
plt.grid()
plt.legend(["$f(x)= x^2$"])
plt.show()