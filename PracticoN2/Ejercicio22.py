"""
Suma los dígitos de un número ingresado por el usuario de forma recursiva.  
Ejemplo: el usuario ingresa 1596  
El programa debe sumar 1 + 5 + 9 + 6  
"""
def sumaDigitos(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sumaDigitos(num // 10)
    
numero = int(input("Ingrese un número: "))
print(sumaDigitos(numero))