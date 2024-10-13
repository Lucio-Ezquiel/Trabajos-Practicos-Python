# Definición de una clase en Python
class Persona:
    def __init__(self, nombre, edad): # Constructor de la clase
        self.nombre = nombre          # Atributo nombre 
        self.edad = edad              # Atributo edad

    def saludar(self):                # Método para saludar
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Creación de objetos (instancias de la clase Persona)
persona1 = Persona("Juan", 25)
persona2 = Persona("Ana", 30)

# Llamada a métodos
persona1.saludar() # "Hola, me llamo Juan y tengo 25 años."
persona2.saludar() # "Hola, me llamo Ana y tengo 30 años. "