"""
Escribe un programa que permita al usuario ingresar una lista y la invierta.
"""
print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
lista.reverse()
print(lista)
