"""
Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
elementos duplicados. 
Pista: 
 Utiliza la función set(). 
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))
resultado = []

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

resultado = set(listaNum)
print("La lista sin números duplicados es: ",resultado)