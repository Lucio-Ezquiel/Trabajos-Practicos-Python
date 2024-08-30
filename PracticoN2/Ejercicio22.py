"""
Suma los dígitos de un número ingresado por el usuario de forma recursiva.  
Ejemplo: el usuario ingresa 1596  
El programa debe sumar 1 + 5 + 9 + 6  
"""
def sumaNum(num):
    suma = 0
    for digito in str(num):
        suma = suma + int(digito)
    return suma
    
num = int(input("Ingrese un número, en lo posible de más de 2 digitos: "))
print("La suma de sus digitos son: ", sumaNum(num))