"""
16- Codifique un método que reciba como parámetro una cadena y determine si la
misma contiene o no números.
"""
cad = input("Ingrese una cadena: ")

class clasify(str):
    def hasNumber(self, strng):
        for i in range(len(strng)):
            if strng[i:i+1].isdigit():
                return True
        return False
cad = clasify(cad)
print(cad.hasNumber(cad))
