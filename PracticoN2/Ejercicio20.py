class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def sumaFracciones(self, fraccion1, fraccion2):
        return fraccion1 + fraccion2
    def restarFracciones(self, fraccion1, fraccion2):
        return fraccion1 - fraccion2
    def multiplicarFracciones(self, fraccion1, fraccion2):
        return fraccion1 * fraccion2
    def dividirFracciones(self, fraccion1, fraccion2):
        return fraccion1 / fraccion2

class OperacionesFraccion:
    def main():
        num1 = int(input("Ingrese su primer valor entero: "))
        num2 = int(input("Ingrese su segundo valor entero: "))
        num3 = int(input("Ingrese su tercer valor entero: "))
        num4 = int(input("Ingrese su cuarto valor entero: "))
        
        fraccion1 = Fraccion(num1, num2)
        fraccion2 = Fraccion(num3, num4)

        suma = fraccion1.sumaFracciones(fraccion2)
        resta = fraccion1.restarFracciones(fraccion2)
        multi = fraccion1.multiplicarFracciones(fraccion2)
        divi = fraccion1.dividirFracciones(fraccion2)

if __name__ == "__main__":
    operaciones = OperacionesFraccion()
    OperacionesFraccion.main()