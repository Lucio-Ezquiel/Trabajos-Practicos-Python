"""
a) Imprime el nombre del alumno2. 
b) Imprime la nota del alumno3. 
"""
alumnos = {
    "alumno1": {"nombre": "Carlos", "edad": 20, "nota": 8.5},
    "alumno2": {"nombre": "Lucia", "edad": 22, "nota": 9.0},
    "alumno3": {"nombre": "Ana", "edad": 21, "nota": 7.5},
}

print(alumnos["alumno2"]["nombre"])
print(alumnos["alumno3"]["nota"])