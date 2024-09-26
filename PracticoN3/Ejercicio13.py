"""
 Explique y ejemplifique la librería NumPy para trabajar con matrices y 
arrays:
NumPy es la abreviatura de "Numerical Python". NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.
"""
#Nota mental: hay que instalar la libreria para que funcione.
import numpy as np
# Array de una dimensión
a1 = np.array([1, 2, 3])
print(a1)
# Array de dos dimensiones
a2 = np.array([[1, 2, 3], [4, 5, 6]]) 
print(a2)
# Array de tres dimensiones
a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a3)