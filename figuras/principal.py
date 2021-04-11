  
from punto import Punto
from circulo import Circulo
from cuadrado import Cuadrado
from triangulo import Triangulo


p1 = Punto(1, 1)
p2 = Punto(2, 6)

opcion = input("Con que figura desea trabajar \n 1. Cuadrado \n 2. Circulo \n 3. Triangulo ")

if opcion == '1':
    figura = Cuadrado(p1, p2)
elif opcion == '2':
    figura = Circulo(p1, p2)
else: 
    figura = Triangulo(p1, p2)

figura.calcular_area()
figura.mostrar_area()
figura.calcular_perimetro()
figura.mostrar_perimetro()