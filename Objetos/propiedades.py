class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre

persona = Persona("Pedro", 25)
print(persona.nombre)  # "Pedro"
persona.nombre = "Juan"
print(persona.nombre)  # "Juan"    