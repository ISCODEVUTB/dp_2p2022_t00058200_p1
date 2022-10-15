from personajes import Personajes
from abc import ABC, abstractmethod


class AbstractPersonajeFactory(ABC):

    @abstractmethod
    def createPersonaje(self, **kwargs)->Personajes:
        pass