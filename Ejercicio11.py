#Ejercicio 11: Crear un programa que genere una lista de números pares entre 1 y 100.

numeros = []
for num in range(2,101,2):
  numeros.append(num)

print("La lista de números pares entre 1 y 100 es",numeros)
