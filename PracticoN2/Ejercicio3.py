"""
Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
14. Plantee el algoritmo planteando métodos para su resolución.
"""
num = input("Ingrese un número de 3 dígitos (100-999): ")

try:
    num = int(num)
    if 100 <= num <= 999:
        suma = 0
        while num > 0:
            digito = num % 10
            suma += digito
            num //= 10
        print("El resultado de la suma de sus dígitos es:", suma)
    else:
        print("El número debe tener 3 dígitos y estar entre 100 y 999")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero de 3 dígitos.")