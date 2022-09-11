from abc import ABCMeta, abstractmethod
from caracterizacion import  Caracterizacion

class IFicha(metaclass=ABCMeta):

    @abstractmethod
    def add(self, caracterizacion: Caracterizacion):
        pass

    @abstractmethod
    def league(self, liga: str):
        pass

    @abstractmethod
    def enemy(self, personaje):
        pass
