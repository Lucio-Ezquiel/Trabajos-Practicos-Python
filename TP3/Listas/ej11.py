"""
Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
cuántas veces aparece ese número en la lista.
"""
print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
num = int(input("Indique numero: "))
print(lista.count(num))
