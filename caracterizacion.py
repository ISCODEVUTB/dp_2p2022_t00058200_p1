from abc import ABC
class Caracterizacion(ABC):
    _name_caracterizacion: str

    def __init__(self, name_caracterizacion):
        self._name_caracterizacion = name_caracterizacion

    @property
    def name_caraterizacion(self) -> str:
        return self._name_caracterizacion

    @name_caraterizacion.setter
    def name_caraterizacion(self, name_caracterizacion: str) -> str:
        self._name_caracterizacion = name_caracterizacion
