"""
Escribe un programa que pida al usuario una lista de números y encuentre el mayor y
el menor de ellos.
"""
print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
print(f"Mayor: {max(lista)}, Menor: {min(lista)}")
