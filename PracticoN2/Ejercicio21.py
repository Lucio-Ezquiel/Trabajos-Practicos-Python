"""
Codifique un programa que solicite un número entero mayor a cero y que 
mediante recursión sume todos los números números naturales desde el número 
ingresado hasta 1.  
Ejemplo: Ingreso 10  
El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 + 1  
"""
def sumaNum (num):
    suma = 0
    for i in range(1, num - 1):
        suma = suma + num
    return suma

num = int(input("Ingrese un número entero mayor a 0: "))
print("El resultado de la suma es: ", sumaNum(num))