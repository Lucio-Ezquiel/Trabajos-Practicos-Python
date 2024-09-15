"""
20- Cree una clase Fracción con dos atributos, numerador y denominador.
Agregue a la clase los siguientes 4 métodos e implemente los mismos:
sumarFracciones(Fraccion f1, Fraccion f2)
restarFracciones(Fraccion f1, Fraccion f2)
multiplicarFracciones(Fraccion f1, Fraccion f2)
dividirFracciones(Fraccion f1, Fraccion f2)
Todos los métodos deben retornar la fracción resultante de la operación.
Cree una clase OperacionesFraccion que contenga un método main donde se solicite
al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos
Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos
implementados anteriormente asignando el resultado a una nueva variable de tipo
Fracción y mostrando por pantalla el resultado de las operaciones realizadas.
"""
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def sumarFracciones(self, f1, f2):
        return Fraccion(f1.numerador * f2.denominador + f2.numerador * f1.denominador, f1.denominador * f2.denominador)

    def restarFracciones(self, f1, f2):
        return Fraccion(f1.numerador * f2.denominador - f2.numerador * f1.denominador, f1.denominador * f2.denominador)

    def multiplicarFracciones(self, f1, f2):
        return Fraccion(f1.numerador * f2.numerador, f1.denominador * f2.denominador)

    def dividirFracciones(self, f1, f2):
        return Fraccion(f1.numerador * f2.denominador, f1.denominador * f2.numerador)

class OperacionesFraccion:
    def main(self):
        self.n1 = int(input("Ingrese un numero: "))
        self.n2 = int(input("Ingrese un numero: "))
        self.n3 = int(input("Ingrese un numero: "))
        self.n4 = int(input("Ingrese un numero: "))

        self.f1 = Fraccion(self.n1, self.n2)
        self.f2 = Fraccion(self.n3, self.n4)

        self.f3 = self.f1.sumarFracciones(self.f1, self.f2)
        self.f4 = self.f1.restarFracciones(self.f1, self.f2)
        self.f5 = self.f1.multiplicarFracciones(self.f1, self.f2)
        self.f6 = self.f1.dividirFracciones(self.f1, self.f2)
        #self.f4 = Fraccion(self.f2.sumarFracciones(self.f2.numerador, self.f2.denominador)

        print(self.f3)
        print(self.f4)
        print(self.f5)
        print(self.f6)

i = OperacionesFraccion()
i.main()
