  
from punto import Punto
from circulo import Circulo
from cuadrado import Cuadrado

cuadrado = Cuadrado(Punto(1, 1), Punto(2, 6))
cuadrado.calcular_area()

cuadrado.mostrar_area()

circulo = Circulo(Punto(10, 10), Punto(5, 5))
circulo.calcular_area()

circulo.mostrar_area()