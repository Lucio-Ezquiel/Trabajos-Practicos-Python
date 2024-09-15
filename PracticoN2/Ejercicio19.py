"""
Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un
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
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.nombre_operacion = None

    
    def sumarNumeros(self):
        return self.valor1 + self.valor2
    
    def restarNumeros(self):
        return self.valor1 - self.valor2
    
    def multiplicarNumeros(self):
        return self.valor1 * self.valor2
    def dividirNumeros(self):
        if(self.valor2 == 0):
            return "No se puede divir por 0"
        else:
            return self.valor1 / self.valor2
        
    def aplicarOperacion(self, nombre_operacion):
        self.nombre_operacion = nombre_operacion
        if self.nombre_operacion == '+':
            return self.sumarNumeros()
        elif self.nombre_operacion == '-':
            return self.restarNumeros()
        elif self.nombre_operacion == '*':
            return self.multiplicarNumeros()
        elif self.nombre_operacion == '/':
            return self.dividirNumeros()
        else:
            return "Operacion no registrada"
            
class Calculo: 
    def main(self):
        operacion = OperacionMatematica(2,3)

        print(f'Suma: {operacion.aplicarOperacion('+')}')
        print(f'Resta: {operacion.aplicarOperacion('-')}')
        print(f'Multiplicación: {operacion.aplicarOperacion('*')}')
        print(f'División: {operacion.aplicarOperacion('/')}')
        

if __name__ == "__main__":
    calculo = Calculo()
    calculo.main()