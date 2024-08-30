""""
CASTEO: Codifique un programa que solicite el ingreso de un numero decimal y 
asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
convertir la variable a los siguientes tipos de datos, short, int, long, float investigue las 
diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las 
conversiones. 
"""
valorDecimal = float(input("Ingrese un número decimal: "))

# Short es como si fuera un int.
short_value = int(valorDecimal)

# Conversión a int.
int_value = int(valorDecimal)

# Conversión a long (similar a int en Python moderno).
long_value = int(valorDecimal)

# Conversión a float.
float_value = valorDecimal

print("Valor original:", valorDecimal)
print("Como short (int):", short_value)
print("Como int:", int_value)
print("Como long (int):", long_value)
print("Como float:", float_value)

