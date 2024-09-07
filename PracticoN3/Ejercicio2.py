"""
Escribe un programa que pida al usuario una lista de números y encuentre el mayor y 
el menor de ellos.
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

print("El mayor número de la lista es: ", max(listaNum))
print("El menor número de la lista es: ", min(listaNum))