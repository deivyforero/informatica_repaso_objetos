from math import sqrt

class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        return sqrt(((self.x - otro_punto.x) ** 2) + ((self.y - otro_punto.y) ** 2))
        