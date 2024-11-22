from Mamifero import Mamifero

class Leon(Mamifero):
    def __init__(self, nombre, edad, peso, color_pelaje, melena):
        super().__init__(nombre, edad, peso, color_pelaje)
        self.melena = melena

    def rugir(self):
        print(f"{self.nombre} está rugiendo.")
