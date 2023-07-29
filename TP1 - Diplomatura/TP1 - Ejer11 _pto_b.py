# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:09:18 2022

@author: Lisandro
"""

# =============================================================================
# 11.Grafique
# b)
# f1(x) = e^x
# f2(x) = 10^x
# f3(x) = 1.7^x en [3; 3]
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3)

fig = plt.figure() 
fig.set_size_inches(10, 6)

plt.ylim(-.1, 10)
plt.plot(x, pow(np.e, x))
plt.plot(x, pow(10, x))
plt.plot(x, pow(1.7, x))
plt.grid()
plt.legend(["$f(x)=e^x$", "$g(x)=10^x$", "$h(x)=1.7^x$"])
plt.show()