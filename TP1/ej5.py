"""
5) Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es,
también debemos indicarlo.
"""
numero = int(input("Ingrese un numero: "))
if (numero % 2 == 0):
    print("Divisible entre 2")
else:
    print("No divisible entre 2")
