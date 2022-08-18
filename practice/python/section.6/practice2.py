

from select import select


class Alumno:
    _nombre = ""
    _nota = 0

    def __init__(self) -> None:
        self._nombre = ""
        self._nota = 0

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNota(self):
        return self._nota

    def setNota(self, nota):
        self._nota = nota

    def imprimirNombre(self):
        return print(self._nombre)

    def imprimirNota(self):
        return print(self._nota)

    def haAprobado(self):
        if (self._nota < 7):
            print(self._nombre + " ha reprobado con " + str(self._nota))
        else:
            print(self._nombre + " ha aprobado con " + str(self._nota))


gabriel = Alumno()
gabriel.setNombre("Gabriel")
gabriel.setNota(8)
gabriel.haAprobado()

daniel = Alumno()
daniel.setNombre("Daniel")
daniel.setNota(5)
daniel.haAprobado()
