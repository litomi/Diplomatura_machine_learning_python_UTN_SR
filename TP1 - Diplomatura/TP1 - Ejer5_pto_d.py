# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:50:07 2022

@author: Lisandro
"""

# =============================================================================
# 5.Grafique
#     
# d)
#     f1(x) = x**1/2
#     f2(x) = x**1/3 en [-3, 3] (ojo)
# 
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)

fig = plt.figure()
fig.set_figwidth(8)
fig.set_figheight(6)

plt.plot(x, np.sqrt(x))
plt.plot(x, np.cbrt(x))
plt.grid()
plt.legend([r"$\sqrt[2]{x}$", r"$\sqrt[3]{x}$"])
plt.show()