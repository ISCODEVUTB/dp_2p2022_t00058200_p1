from personajesfactory import AbstractPersonajeFactory
from humanos import Humanos


class FactoryHumanos(AbstractPersonajeFactory):

    def createPersonaje(self, **kwargs):
        return Humanos(**kwargs)