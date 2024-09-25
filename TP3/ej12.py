"""
Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud.
"""
print("Presione q para terminar de ingresar numeros.")
def ingLista():
    l = []
    while True:
        n = input("Ingrese un numero o q: ")
        if n == "q":
            break
        l.append(int(n))
    return l

lista1 = ingLista()
print(lista1)
lista2 = ingLista()

if len(lista1) != len(lista2):
    print("Tamaños diferentes")
else:
    print([lista1[i] * lista2[i] for i in range(len(lista1))])
