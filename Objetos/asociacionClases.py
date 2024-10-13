class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coche = None  # No necesariamente tiene coche cuando se crea

    def asignar_coche(self, coche):
        self.coche = coche

    def mostrar_info(self):
        if self.coche:
            print(f"{self.nombre} tiene un coche {self.coche.marca} {self.coche.modelo}.")
        else:
            print(f"{self.nombre} no tiene coche.")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Creando los objetos
persona1 = Persona("Carlos")
coche1 = Coche("Toyota", "Corolla")

# Asociando la persona con su coche
persona1.asignar_coche(coche1)

# Mostrando la información
persona1.mostrar_info()  # Output: Carlos tiene un coche Toyota Corolla.