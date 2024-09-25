"""
Escribe un programa que permita al usuario ingresar una lista de números y elimine los
elementos duplicados.
Pista:
Utiliza la función set().
"""
print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
print(set(lista))
