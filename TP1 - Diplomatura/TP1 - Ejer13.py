# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:21:58 2022

@author: Lisandro
"""

# =============================================================================
# 13.Promedio Ponderado: Pida 5 notas de un alumno. Asigne distinto porcentaje
# de importancia a cada nota, suponiendo que la nota 1 y la 3 son las menos 
# importantes ya que refieren a peque~nos controles de avance hogare~nos. 
# La nota 2 y la 4 son intermedias en importancia (refieren a entrega de 
# proyectos) y la nota 5 es muy importante ya que refiere a un examen global. 
# El porcentaje total entre las 5 notas, su importancia, debería sumar
# el 100 %. Calcule el promedio ponderado.
# =============================================================================
def prom_ponderado(notas, pesos):
    suma = 0
    ponderaciones = 0
    for i in range(len(notas)):
        ponderaciones += pesos[i]
        suma += notas[i] * pesos[i]    
    return suma / ponderaciones

import sys
pesos = [.05, .15, .05, .15, .6 ]
notas = []

print("Ingrese las notas sucesivamente(0.00 - 10.00).")
for i in range(5):
    while True:
        sys.stdout.flush()       
        try:            
            opc = float(input(("%d -> ") % (i + 1)))
            if opc < 0 or opc > 10:
                print("Sólo entradas entre 0.00 y 10.00\n")
                continue
            notas.append(opc)
            break
        except:
           print("Sólo decimales. ")

print("Promedio del alumno: ", prom_ponderado(notas, pesos))