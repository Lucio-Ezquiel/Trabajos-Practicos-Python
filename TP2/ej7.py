"""
7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total.
"""
cad = input("Ingrese una cadena: ")
print(f"Total: {len(cad)}, Vocales: {sum(cad.lower().count(vocal) for vocal in "aeiou")}")
