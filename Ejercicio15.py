# Ejercicio #15
frase = input("Escribe una frase: ")

def palindromo(palabra):
  palabra = palabra.lower() # hace que también se puedan ingresar letras tanto minusculas como mayusculas
  return palabra == palabra[::-1]

if palindromo(frase):
  print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")