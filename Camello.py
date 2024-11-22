from Mamifero import Mamifero

class Camello(Mamifero):
    def __init__(self, nombre, edad, peso, color_pelaje, jorobas):
        super().__init__(nombre, edad, peso, color_pelaje)
        self.jorobas = jorobas

    def almacenar_agua(self):
        print(f"{self.nombre} está almacenando agua en sus jorobas.")

