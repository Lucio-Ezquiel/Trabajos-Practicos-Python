"""
9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII.
Muéstralos en línea recta, separados por un espacio entre cada carácter.
"""
cad = "La lluvia en Mendoza es escasa"
for c in cad:
    print(ord(c), end=" ")
print()
