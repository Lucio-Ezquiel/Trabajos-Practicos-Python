def es_dia_laboral():
    while True:
        try:
            dia_semana = int(input("Ingrese un número del 1 al 7 para representar un día de la semana: "))
            if 1 <= dia_semana <= 7:
                break
            else:
                print("Número inválido. Ingrese un número entre 1 y 7.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    if 1 <= dia_semana <= 5:
        print("Es un día laboral.")
    else:
        print("Es un día no laboral.")

es_dia_laboral()