"""
Escribe un programa que permita al usuario ingresar una lista y la invierta. 
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

listaNum.reverse()
print("La lista de números invertida es: ", listaNum)