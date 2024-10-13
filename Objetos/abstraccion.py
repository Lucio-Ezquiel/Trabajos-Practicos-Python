from abc import ABC, abstractmethod

class figuraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class cuadrado(figuraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

# No se puede instanciar una clase abstracta
# figura = figuraGeometrica() # Error

cuadrado = cuadrado(4)
print(cuadrado.area())  # "16"