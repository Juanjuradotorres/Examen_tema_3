from Ornitorrinco import Ornitorrinco

class OrnitorrincoMacho(Ornitorrinco):
    def __init__(self, nombre, edad, peso, color_pelaje, cantidad_huevos, cola_castor, espolones):
        super().__init__(nombre, edad, peso, color_pelaje, cantidad_huevos, cola_castor)
        self.espolones = espolones

    def inyectar_veneno(self):
        print(f"{self.nombre} está inyectando veneno con sus espolones.")
