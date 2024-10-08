"""
Cree una clase FuncionesPrograma y codifique una función estática getFechaString
que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
Ejemplo recibo 15/10/1900, la salida debe ser
Quince de Octubre de mil novecientos.
"""
class FuncionesPrograma:
    @staticmethod
    def getFechaString(fecha):
        # diccionarios generadas con AI. 
        units = {
            0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
            5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
        }

        tens = {
            10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce",
            15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
            20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta",
            60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa"
        }

        hundreds = {
            100: "cien", 200: "doscientos", 300: "trescientos", 400: "cuatrocientos",
            500: "quinientos", 600: "seiscientos", 700: "setecientos", 800: "ochocientos", 900: "novecientos"
        }

        months = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
            6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre",
            10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        dayi, monthi, yeari = fecha.split("/")
        
        def tweens(value):
            if int(value) > 20 and int(value) % 10 != 0:
                return tens[int(value) - (int(value) % 10)] + units[int(value) % 10] 
            elif int(value) > 9:
                return tens[int(value)] 
            else:
                return units[int(value)] 
            
        # Start with day.
        dayi = tweens(dayi)
        # Month
        monthi = months[int(monthi)]
        # Year
        yeari = list(yeari)
        if yeari[1] != '0':
            yeari[1] = ' ' + hundreds[int(yeari[1]) * 100]
        else:
            yeari[1] = ''
        if yeari[2] != '0':
            yeari[2] = ' ' + tweens(yeari[2] + yeari[3])
        else:
            yeari[2] = ''
        if int(yeari[0]) > 1:
            yeari[0] = ' ' + units[int(yeari[0])]
        else:
            yeari[0] = ''

        return (f"{dayi.capitalize()} de {monthi} de{yeari[0]} mil{yeari[1]}{yeari[2]}")


class Principal:
    def main():
        print(FuncionesPrograma.getFechaString("15/10/1900"))
        print(FuncionesPrograma.getFechaString("15/10/2024"))
        print(FuncionesPrograma.getFechaString("17/10/3335"))

Principal.main()