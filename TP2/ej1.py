"""
CASTEO: Codifique un programa que solicite el ingreso de un numero decimal y
asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para
convertir la variable a los siguientes tipos de datos, short, int, long, float investigue las
diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las
conversiones.
"""
valorDecimal = input("Ingrese numero decimal: ")

print(f"Type: {type(int(float(valorDecimal)))}, Value: {int(float(valorDecimal))}")
print(f"Type: {type(float(valorDecimal))}, Value: {float(valorDecimal)}")

# No pongo short ni long como no son numeros en python
