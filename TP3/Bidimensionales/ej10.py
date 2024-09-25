"""
Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique
si una matriz es simétrica.
"""
import numpy
m = numpy.array([[6, 12, 18], [5, 11, 17], [4, 10, 16], [3, 9, 15], [2, 8, 14], [1, 7, 13]])
#m = numpy.array([[6, 12, 18, 20], [12, 4, 10, 15], [18, 10, 13, 2], [20, 15, 2, 4]])
print(m)
print(numpy.array_equal(m, m.T) and ("Simetrico") or ("No simetrico"))
