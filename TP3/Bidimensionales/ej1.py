"""
Crea una función que reciba dos parámetros: el número de filas y columnas. La función
debe generar una matriz de ese tamaño, donde los valores son números enteros
consecutivos empezando desde 1.
"""
def crear(filas, columnas):
    m = []
    for f in range(1,filas+1):
        m.append(list(range((f-1)*columnas+1,f*columnas+1)))
    return m

f = int(input("Ingrese numero de filas: "))
c = int(input("Ingrese numero de columnas: "))

print(crear(f,c))
