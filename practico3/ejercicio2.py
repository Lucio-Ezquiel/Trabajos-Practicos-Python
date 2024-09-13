'''
Escribe un programa que pida al usuario una lista de números y encuentre el mayor y el menor de ellos. 
'''

def ingresar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Valor no válido. Por favor ingrese un número entero")

def desea_continuar():
    while True:
        decision = input("¿Desea ingresar otro número? (s/n): ").strip().lower()
        if decision in ['s', 'n']:
            return decision == 's'
        print("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no.")

def main(): 
    numeros = []

    while True:
        numero = ingresar_numero()
        numeros.append(numero)

        if not desea_continuar():
            break
    
    nroMaximo = max(numeros)
    nroMinimo = min(numeros)

    print(f'El mayor número ingresado es {nroMaximo} y el menor es {nroMinimo}')

if __name__ == '__main__':
    main()