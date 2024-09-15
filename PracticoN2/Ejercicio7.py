"""
Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total.
"""
vocales = "aeiou"
cadena = str(input("Ingrese una cadena: "))
tamaño = len(cadena)

num_vocales = 0
for vocal in vocales:
    num_vocales += cadena.count(vocal)

print("El tamaño de la cadena es:", tamaño)
print("La cadena tiene:", num_vocales, "vocales.")