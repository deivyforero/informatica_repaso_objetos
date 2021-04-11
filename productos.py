class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "static/imagenes/humanos/arma.png"
        self.descripcion = "arma del humano"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/arma.png"
        self.descripcion = "arma del orco"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "static/imagenes/humanos/escudo.png"
        self.descripcion = "escudo humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/escudo.png"
        self.descripcion = "escudo orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)


class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "static/imagenes/orcos/montura.jpg"
        self.descripcion = "montura orcos"


class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "static/imagenes/humanos/montura.jpg"
        self.descripcion = "montura humanos"

#------------------------------------------------------------Fabrica 2------------------------------------
class Cuerpo:
    def __init__(self):
        self.brazos = ""
        self.piernas = ""
        self.cabeza = ""
        self.torso = ""
        self.imgcuerpo = ""

class Cuerpo1(Cuerpo):
    def __init__(self):
        Cuerpo.__init__(self)

class CuerpoHumano(Cuerpo1):
    def __init__(self):
        self.brazos = "Fuertes"
        self.piernas = "Largas"
        self.cabeza = "Pequeña"
        self.torso = "Grande"
        self.descripcion = "Cuerpo Humano"
        self.imgcuerpo = "static/imagenes/humanos/Cuerpo.jpg"

class CuerpoOrco(Cuerpo1):
    def __init__(self):
        self.brazos = "feos"
        self.piernas = "Feos"
        self.cabeza = "Feos"
        self.torso = "Feos"
        self.descripcion = "Cuerpo Orco"
        self.imgcuerpo = "static/imagenes/orcos/Cuerpo.jpg"

