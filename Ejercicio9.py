# Ejercicio 9: Crear un programa que genere una matriz de números y la imprima en pantalla.

import numpy as np

matriz =np.zeros((4,5))
def matrix(i,j):
  return i*j

for i in range(4):
    for j in range(5):
        matriz[i][j] = matrix(i,j)

print(f"La matriz de numeros es:\n",matriz)