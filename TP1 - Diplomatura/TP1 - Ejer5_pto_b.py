# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:45:48 2022

@author: Lisandro
"""

# =============================================================================
# 5.Grafique
#     
# b) 
#     f1(x) = 2x^2 
#     f2(x) = 3x^2
#     f3(x) = 4x^2 en [-2, 2]
# 
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 2, 0.01)

f1 = [2*x**2 for x in x]
f2 = [2*x**3 for x in x]
f3 = [4*x**2 for x in x]

fig = plt.figure()
fig.set_figheight(10)
fig.set_figwidth(8)

plt.plot(x, f1)
plt.plot(x, f2)
plt.plot(x, f3)
plt.grid()
plt.legend(["f(x)=$2x^{2}$", "g(x)=$2x^{3}$", "h(x)=$4x^{2}$"])
plt.show()