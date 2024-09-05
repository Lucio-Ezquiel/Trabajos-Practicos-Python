"""
3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
14. Plantee el algoritmo planteando métodos para su resolución.
"""
while True:
    numero = int(input("Ingrese un numero de 3 digitos (100 - 999): "))
    if 100 <= numero < 1000: break
    
s = 0
while numero:
    s += numero % 10
    numero = numero // 10
print(s)
