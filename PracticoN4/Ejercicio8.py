"""
a) Elimina la clave edad del diccionario. 
b) Imprime el diccionario después de eliminar esa clave. 
"""
mascota = {"nombre": "Firulais", "especie": "Perro", "edad": "5"}

mascota.pop("edad")
print(mascota)