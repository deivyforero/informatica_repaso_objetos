  
from punto import Punto

class Figura:
    def __init__(self, p1, p2):
        self.punto_uno = p1
        self.punto_dos = p2
        self.area = 0
        self.perimetro = 0
        self.nombre = ""

    def mostrar_area(self):
        print("El area del " + self.nombre + " es: " + str(self.area))

    def mostrar_perimetro(self):
        print("El perimetro del " + self.nombre + " es: " + str(self.perimetro))