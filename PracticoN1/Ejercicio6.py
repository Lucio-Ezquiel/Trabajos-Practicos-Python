print("Introduzca el precio de su producto para calcular su precio final con IVA (21%)")
precioInicial = input()
precioInicial = float(precioInicial)
precioFinal = precioInicial * 1.21
print(precioFinal)

print("ingrese un numero mayor a 0: ")
num = input()

while (num <= 0):
    print("ingrese un numero mayor a 0: ")
    num = input()
