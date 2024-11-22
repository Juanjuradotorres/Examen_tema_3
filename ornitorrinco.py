from Mamifero import Mamifero
from Oviparo import Oviparo

class Ornitorrinco(Oviparo, Mamifero):  # Hereda de Oviparo y Mamifero
    def __init__(self, nombre, edad, peso, color_pelaje, cantidad_huevos, cola_castor):
        # Inicializamos las clases base explícitamente
        Mamifero.__init__(self, nombre, edad, peso, color_pelaje)
        Oviparo.__init__(self, nombre, edad, peso, cantidad_huevos)
        self.cola_castor = cola_castor

    def construir_madriguera(self):
        print(f"{self.nombre} está construyendo una madriguera con su cola de castor.")

