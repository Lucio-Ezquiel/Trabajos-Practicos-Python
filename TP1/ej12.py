"""
12) Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
nuevamente
"""
while True:
    dia = input("Ingrese un dia representado por su numero: ")
    match dia:
        case "1":
            print(f"Lunes ({dia}) es dia laboral.")
            break
        case "2":
            print(f"Martes ({dia}) es dia laboral.")
            break
        case "3":
            print(f"Miercoles ({dia}) es dia laboral.")
            break
        case "4":
            print(f"Jueves ({dia}) es dia laboral.")
            break
        case "5":
            print(f"Viernes ({dia}) es dia laboral.")
            break
        case "6" | "7":
            print("No es dia laboral.")
            break
        case _:
            print("No es input acceptado.")
