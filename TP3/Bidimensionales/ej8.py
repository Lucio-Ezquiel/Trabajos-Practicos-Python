"""
Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad
es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto
son 0.
"""
import numpy

n = int(input("Ingrese tamaño de n: "))

m = numpy.identity(n, dtype = int)
print(m)
