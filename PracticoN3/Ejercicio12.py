"""
Escribe un programa que sume dos listas de números elemento por elemento. Las 
listas deben tener la misma longitud.
"""
lista1 = [1,2,3,4,5]
lista2 = [2,4,6,8,10]
sumaLista = []

if len(lista1) == len(lista2):
    for i in range(len(lista1)):
        suma = lista1[i]+lista2[i]
        sumaLista.append(suma)
    print("La suma de elemento a elemento de la listas es:",sumaLista)
else:
    print("Las listas no tienen la misma cantidad de números")

