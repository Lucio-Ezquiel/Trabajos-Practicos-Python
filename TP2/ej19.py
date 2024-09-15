"""
19- Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un
atributo de nombre operación.
Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
sumarNumeros()
restarNumeros()
multiplicarNumeros()
dividirNumeros()
El quinto método será el siguiente:
aplicarOperacion(operacion){
…………………..
}
Cree una clase Calculo que contenga un método main, donde cree una instancia de la
clase OperacionMatematica, asigne 2 valores para las variables de la instancia y
ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “-
”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las
operaciones.
"""

class OperacionMatematica():
    def __init__(self, valor1, valor2, operacion='+'):
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
        return self.valor1 / self.valor2

    def aplicarOperacion(self, operacion):
        match operacion:
            case "+":
                return self.sumarNumeros()
            case "-":
                return self.restarNumeros()
            case "*":
                return self.multiplicarNumeros()
            case "/":
                return self.dividirNumeros()

class Calculo():
    def main(self):
        op = OperacionMatematica(8,4)
        add = op.aplicarOperacion('+')
        sub = op.aplicarOperacion('-')
        mult = op.aplicarOperacion('*')
        div = op.aplicarOperacion('/')

        print(f"sumar: {add}, restar: {sub}, multiplicar: {mult}, division: {div}")

i = Calculo()
i.main()
