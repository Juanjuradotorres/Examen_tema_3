from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, peso, color_pelaje):
        super().__init__(nombre, edad, peso)
        self.color_pelaje = color_pelaje

    def amamantar(self):
        print(f"{self.nombre} está amamantando a sus crías.")
