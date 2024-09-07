"""
Escribe un programa que permita al usuario ingresar una lista de números y eliminar 
un elemento en un índice especificado. 
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))
n2 = int(input("Ingrese que posición de la lista quiere borrar: "))

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

if 0 <= n2 < len(listaNum):
    eliminada = listaNum.pop(n2)
    print("El elemento eliminado es:", eliminada)
    print("La lista con esa posición eliminada es: ", listaNum)
else:
    print("Índice fuera de rango.")