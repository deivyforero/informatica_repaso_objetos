from figura import Figura

class Cuadrado(Figura):
    
    def __init__(self, p1, p2):
        Figura.__init__(self, p1, p2)
        self.nombre = "Cuadrado"
    
    def calcular_area(self):
        lado = self.punto_uno.calcular_distancia(self.punto_dos)
        self.area = lado ** 2

    def calcular_perimetro(self):
        lado = self.punto_uno.calcular_distancia(self.punto_dos)
        self.perimetro = 4 * lado