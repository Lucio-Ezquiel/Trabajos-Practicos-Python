"""
Codifique un método que reciba como parámetro una cadena y determine si la
misma contiene o no números
"""
def contiene_numeros(cadena):
    return any(char.isdigit() for char in cadena)

cadena = str(input("Ingrese una cadena: "))
print(contiene_numeros(cadena))