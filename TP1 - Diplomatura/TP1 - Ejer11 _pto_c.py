# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:14:33 2022

@author: Lisandro
"""

# =============================================================================
# 11.Grafique
# c) f(x) = 1/x en [-2, 2]
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 300)
x = [np.nan if i > -np.diff(x)[0] and i < np.diff(x)[0] else 1/i for i in x]

fig = plt.figure() 
fig.set_size_inches(10, 7)

plt.plot(x)
plt.grid()
plt.legend(([r"$f(x) = \frac{1}{x}$"]))
plt.show()
