"""
Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de números y calcule el
promedio de los elementos.
"""
print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
print(f"Promedio: {sum(lista)/len(lista)}")
