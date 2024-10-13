class Ave:
    def volar(self):
        print("El ave está volando")

class Pinguino(Ave):
    def volar(self):
        print("El pinguino no puede volar, pero puede nadar")

def hacer_volar(ave):
    ave.volar()

pajaro = Ave()
pinguino = Pinguino()

hacer_volar(pajaro)    # "El ave está volando"
hacer_volar(pinguino)  # "El pinguino no puede volar, pero puede nadar"