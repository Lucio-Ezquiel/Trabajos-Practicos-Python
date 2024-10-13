class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coche = None  # Inicialmente, la persona no tiene coche

    def asignar_coche(self, coche):
        self.coche = coche
        coche.propietario = self  # El coche ahora sabe quién es su dueño

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.propietario = None  # Inicialmente, el coche no tiene propietario

    def mostrar_info(self):
        if self.propietario:
            print(f"Este {self.marca} {self.modelo} pertenece a {self.propietario.nombre}.")
        else:
            print(f"Este {self.marca} {self.modelo} no tiene propietario.")

# Creando los objetos
persona1 = Persona("Carlos")
coche1 = Coche("Toyota", "Corolla")

# Asociando la persona con su coche y viceversa
persona1.asignar_coche(coche1)

# Mostrando información desde ambos lados
persona1.mostrar_info()  # "Carlos tiene un coche Toyota Corolla."
coche1.mostrar_info()  # "Este Toyota Corolla pertenece a Carlos."