"""
Escribe un programa que multiplique cada elemento de una lista de números por un 
valor ingresado por el usuario. 
"""
listaNum = [1, 2, 3, 4, 5]
n = int(input("Ingrese un valor que multiplicará cada elemento de la lista: "))
resultado = []

for numero in listaNum:
    resultado.append(numero * n)

print("La lista multiplicada por el número ",n,"es: ", resultado)