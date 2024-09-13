'''
Escribe un programa que pida al usuario una lista de números y cuente cuántos de ellos son pares y cuántos son impares. 
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

def son_pares(listaNumeros):
    return len([x for x in listaNumeros if x%2 == 0])

def main():
    numeros = []
    while True:
        numero = ingresar_numero()
        numeros.append(numero)
        
        if not desea_continuar():
            break
        
    cantidadDePares = son_pares(numeros)
    cantidadImpares = len(numeros) - cantidadDePares
    
    print(f'Usted ingresó {cantidadDePares} número pares y {cantidadImpares} números impares.')
    
if __name__ == '__main__':
    main()
    