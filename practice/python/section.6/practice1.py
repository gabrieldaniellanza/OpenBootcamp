

from select import select


class Vehiculo:
    _color = ""
    _ruedas = 0
    _puertas = 0

    def __init__(self) -> None:
        self._color = "Blanco"
        self._ruedas = 1
        self._puertas = 1

    def __init__(self, color, ruedas, puertas) -> None:
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas

    def getColor(self):
        return self._color

    def getRuedas(self):
        return self._ruedas

    def getPuertas(self):
        return self._puertas


class Coche(Vehiculo):
    _velocidad = 0
    _cilindrada = 0

    def __init__(self, color, ruedas, puertas, cilindrada) -> None:
        super().__init__(color, ruedas, puertas)
        self._cilindrada = cilindrada

    def getVelocidad(self):
        return self._velocidad

    def getCilindrada(self):
        return self._cilindrada


c = Coche("Negro", 4, 2, 2.1)

print("Color: " + str(c.getColor()))
print("Cilindrada: " + str(c.getCilindrada()))
print("Puertas: " + str(c.getPuertas()))
print("Ruedas: " + str(c.getRuedas()))
print("Velocidad: " + str(c.getVelocidad()))
