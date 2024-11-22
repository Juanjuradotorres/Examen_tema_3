from Leon import Leon
from Camello import Camello
from Ornitorrinco import Ornitorrinco
from OrnitorrincoMacho import OrnitorrincoMacho

def main():
    # León
    leon = Leon("Nala", 5, 190, "Amarillo", "No tiene")
    print(f"Nombre: {leon.nombre}, Edad: {leon.edad}, Peso: {leon.peso} kg")
    leon.dormir()
    leon.moverse()
    print(f"Color de pelaje: {leon.color_pelaje}")
    leon.amamantar()
    print(f"Tamaño de melena: {leon.melena}")
    leon.rugir()
    print()

    # Camello
    camello = Camello("Camella", 7, 600, "Beige", 2)
    print(f"Nombre: {camello.nombre}, Edad: {camello.edad}, Peso: {camello.peso} kg")
    camello.dormir()
    camello.moverse()
    print(f"Color de pelaje: {camello.color_pelaje}")
    camello.amamantar()
    print(f"Número de jorobas: {camello.jorobas}")
    camello.almacenar_agua()
    print()

    # Crear un Ornitorrinco
    ornitorrinco = Ornitorrinco("Ornitorinca", 3, 2, "Marrón", 2, "Corta")
    print(f"Nombre: {ornitorrinco.nombre}, Edad: {ornitorrinco.edad}, Peso: {ornitorrinco.peso} kg")
    ornitorrinco.dormir()
    ornitorrinco.moverse()
    print(f"Color de pelaje: {ornitorrinco.color_pelaje}")
    ornitorrinco.amamantar()
    print(f"Tamaño de la cola: {ornitorrinco.cola_castor}")
    ornitorrinco.construir_madriguera()

    # Ornitorrinco Macho
    print()
    ornitorrinco_macho = OrnitorrincoMacho("Perry", 3, 2, "Marrón", 2, "Larga", "Afilados")
    print(f"Nombre: {ornitorrinco_macho.nombre}, Edad: {ornitorrinco_macho.edad}, Peso: {ornitorrinco_macho.peso} kg")
    ornitorrinco_macho.dormir()
    ornitorrinco_macho.moverse()
    print(f"Color de pelaje: {ornitorrinco_macho.color_pelaje}")
    ornitorrinco_macho.amamantar()
    print(f"Tamaño de la cola: {ornitorrinco_macho.cola_castor}")
    print(f"Espolones: {ornitorrinco_macho.espolones}")
    ornitorrinco_macho.inyectar_veneno()
    print()

if __name__ == "__main__":
    main()
