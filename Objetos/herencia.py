# Clase Padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass # Método que será sobreescrito en las clases hijas

# Clase Hija
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Clase Hija
class Gato(Animal):
    def hacer_sonido(self):
        return "Guau"

# Uso de herencia
mi_perro = Perro("Bobby")
mi_gato = Gato("Mimi")

print(mi_perro.hacer_sonido()) # "Guau"
print(mi_gato.hacer_sonido())  # "Miau"