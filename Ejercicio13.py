#Ejerci#Ejercicio 13: Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división

#Ejercicio 13: Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división

num1 = int(input("Ingrese un número"))
num2 = int(input("Ingrese otro número"))

def operacion(num1,num2):
  sum = num1+num2
  resta = num1-num2
  mult = num1*num2
  div = num1/num2
  return sum,resta,mult,div

sol = operacion(num1,num2)
print("Las operaciones básicas del numero ingresado son",sol)
