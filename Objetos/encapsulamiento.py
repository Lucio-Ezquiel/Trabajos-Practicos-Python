class Coche:
    def __init__(self, marca, modelo, velocidadMaxima):
        self.marca = marca
        self.__modelo = modelo                   # Atributo privado
        self._velocidadMaxima = velocidadMaxima  # Atrubuto protegido
    
    def mostrar_modelo(self):
        print(f"El modelo es {self.__modelo}")

# Instanciando la clase
mi_coche = Coche("Toyota", "Corolla", 180)
mi_coche.mostrar_modelo() # "El modelo es Corolla"
# Intentar acceder directamente al atributo privado genera un error:
# # print(mi_coche.__modelo) # AttributeError    