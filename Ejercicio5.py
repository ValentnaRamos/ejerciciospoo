#Ejercicio 5: Crear una función que convierta grados Fahrenheit a grados Celsius.

def grados(F):
  celsius = ((F-32)*5)/9
  return celsius

f = 60
conversion = grados(f)
print("Los grados celsius serían",conversion)