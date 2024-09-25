"""
Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido
de las agujas del reloj.
"""
import numpy
m = numpy.array([[6, 12, 18, 20], [12, 4, 10, 15], [18, 10, 13, 2], [20, 15, 2, 4]])
print(m)
print(numpy.rot90(m, k=-1))
