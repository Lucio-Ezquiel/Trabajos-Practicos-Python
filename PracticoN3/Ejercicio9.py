"""
Escribe un programa que permita al usuario ingresar una lista de números y filtre los 
números primos. 
Pista: 
 Usa una función para verificar si un número es primo.
"""
def primo(numero):
  if numero <= 1:
    return False
  if numero <= 3:
    return True
  if numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

listaNum = []
primos = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

for num in listaNum:
    if primo(num):
        primos.append(num)

print("Los números primos son:", primos)
