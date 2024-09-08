"""
Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
debe generar una matriz de ese tamaño, donde los valores son números enteros 
consecutivos empezando desde 1. 
"""
def funcion(filas, columnas):
    matriz=[]
    contador=1
    for _ in range(filas):
        filas=[]
        for _ in range(columnas):
            filas.append(contador)
            contador+=1
        matriz.append(filas)
    return matriz

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

resultado = funcion(filas, columnas)
print(resultado)