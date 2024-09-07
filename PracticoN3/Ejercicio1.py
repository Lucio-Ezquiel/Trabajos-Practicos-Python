"""
Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
suma de todos los elementos en la lista.
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))
sumaLista = 0

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

sumaLista = sum(listaNum)

print("La suma de su lista de números es: ", sumaLista)
