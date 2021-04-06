from math import pi
from figura import Figura

class Circulo(Figura):

    def __init__(self, p1, p2):
        Figura.__init__(self, p1, p2)
        self.nombre = "Circulo"

    def calcular_area(self):
        radio = self.punto_uno.calcular_distancia(self.punto_dos)
        self.area = pi * radio ** 2

    def calcular_perimetro(self):
        radio = self.punto_uno.calcular_distancia(self.punto_dos)
        self.perimetro = 2 * pi * radio