from flask import Flask, render_template
from fabricas import *
from random import choice


app = Flask(__name__)

@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    montura = fabrica.crear_montura()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(montura)

    # Dependiendo del grupo que se seleccione con la funcion aleatoria sabemos que fabrica de cuerpos utilizar
    if arma.grupo == "Humanos":
        fabricas2 = FabricaHumanos2()
    else:
        fabricas2 = FabricaOrcos2()

    cuerpo = fabricas2.crear_cuerpo()
    cuerpos = []
    cuerpos.append(cuerpo)

    return render_template("productos.html", productos = productos, cuerpos = cuerpos)

if __name__ == '__main__':
    app.run(debug=True)