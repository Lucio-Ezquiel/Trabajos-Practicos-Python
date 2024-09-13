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

class OperacionMatematica:
    def __init__(self, valor1, valor2, operacion):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumarNumeros():
        return self.valor1 + self.valor2

    def restarNumeros():
        return self.valor1 - self.valor2

    def multiplicarNumeros():
        return self.valor1 * self.valor2

    def dividirNumeros():
        return self.valor1 / self.valor2

    def aplicarOperacion(operacion):
        match operacion:
            case "+":
                sumarNumeros()
