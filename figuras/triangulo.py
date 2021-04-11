from figura import Figura
from punto import Punto

class Triangulo(Figura):
    
    def __init__(self, p1, p2):
        Figura.__init__(self, p1, p2)
        self.nombre = "Triangulo"
    
    def calcular_area(self):
        punto_temporal = Punto(self.punto_uno.x, self.punto_dos.y)
        lado_uno = self.punto_uno.calcular_distancia(punto_temporal)
        lado_dos = self.punto_dos.calcular_distancia(punto_temporal)
        self.area = lado_uno * lado_dos / 2

    def calcular_perimetro(self):
        punto_temporal = Punto(self.punto_uno.x, self.punto_dos.y)
        hipo = self.punto_uno.calcular_distancia(self.punto_dos)
        lado_uno = self.punto_uno.calcular_distancia(punto_temporal)
        lado_dos = self.punto_dos.calcular_distancia(punto_temporal)
        self.perimetro = hipo + lado_uno + lado_dos