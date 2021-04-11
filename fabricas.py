from productos import *


class Fabrica2:
    def crear_cuerpo(self):
        pass

class FabricaHumanos2(Fabrica2):

    def crear_cuerpo(self):
       return CuerpoHumano()

class FabricaOrcos2(Fabrica2):

    def crear_cuerpo(self):
        return CuerpoOrco()


class Fabrica:

    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

    def crear_montura(self):
        pass

class FabricaHumanos(Fabrica):

    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

    def crear_montura(self):
        return MonturaHumanos()

class FabricaOrcos(Fabrica):

    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

    def crear_montura(self):
        return MonturaOrcos()