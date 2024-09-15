"""
21- Codifique un programa que solicite un número entero mayor a cero y que
mediante recursión sume todos los números números naturales desde el número
ingresado hasta 1.
Ejemplo: Ingreso 10
El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 + 1
"""
def recSuma(num):
    if num == 1:
        return 1
    else:
        return recSuma(num -1) + num
number = int(input("coloque un numero: "))
print(recSuma(number))
