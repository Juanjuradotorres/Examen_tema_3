from Animal import Animal

class Oviparo(Animal):  # Hereda de Animal
    def __init__(self, nombre, edad, peso, cantidad_huevos):
        # Inicializa la clase base Animal
        Animal.__init__(self, nombre, edad, peso)
        self.cantidad_huevos = cantidad_huevos

    def poner_huevos(self):
        print(f"{self.nombre} está poniendo {self.cantidad_huevos} huevos.")
