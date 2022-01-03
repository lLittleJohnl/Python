class Comida:
    def __init__(strogonoff, tipo, acomp):
        strogonoff.tipo = tipo
        strogonoff.acomp = acomp

    def funcao(fome):
        a = ("Eu adoro comer um " + fome.tipo)
        b = (" com " + fome.acomp)
        print(a + b)

prato = Comida("Strogonoff de frango", "coquinha gelada")
del acomp
prato.funcao()