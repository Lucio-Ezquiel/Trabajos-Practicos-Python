"""
Escribe un programa que permita al usuario ingresar una lista de números y eliminar
un elemento en un índice especificado.
"""
print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
    
print(lista)
del lista[int(input("Indique indice del elemento que eliminar: "))]
print(lista)
