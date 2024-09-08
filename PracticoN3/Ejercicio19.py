"""
Escribe un programa que multiplique cada elemento de una lista bidimensional por un 
valor escalar dado por el usuario.
"""
matriz=[[1,2,3],[4,5,6],[7,8,9]]
escalar=int(input("Ingrese un escalar por el cual se multiplicará la matriz bidimensional: "))
resultado=[]

for fila in matriz:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(elemento * escalar)
    resultado.append(nueva_fila)

print("La matriz dimensional multiplicada por el escalar es: ", resultado)