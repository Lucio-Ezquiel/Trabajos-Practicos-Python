"""
Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
promedio de los elementos.
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))
promedio = 0

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

promedio = sum(listaNum)/len(listaNum)
print("El promedio de la suma de los elementos de la lista es: ",promedio)