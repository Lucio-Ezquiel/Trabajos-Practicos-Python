class OperacionMatematica:
    def __init__(self, valor1, valor2, operacion):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = operacion

    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 == 0:
            return "Error: División por cero"
        else:
            return self.valor1 / self.valor2

    def aplicarOperacion(self):
        if self.operacion == "+":
            return self.sumarNumeros()
        elif self.operacion == "-":
            return self.restarNumeros()
        elif self.operacion == "*":
            return self.multiplicarNumeros()
        elif self.operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"

class Calculo:
    def main():
        operacion = OperacionMatematica(10, 5, "+")
        print(operacion.aplicarOperacion())

        operacion.operacion = "-"
        print(operacion.aplicarOperacion())

        operacion.operacion = "*"
        print(operacion.aplicarOperacion())

        operacion.operacion = "/"
        print(operacion.aplicarOperacion())

if __name__ == "__main__":
    Calculo.main()     
    