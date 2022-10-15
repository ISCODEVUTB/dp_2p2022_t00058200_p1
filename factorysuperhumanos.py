from personajesfactory import AbstractPersonajeFactory

from superHumanos import SuperHumanos


class FactorySuperHumanos(AbstractPersonajeFactory):

    def createPersonaje(self, **kwargs):
        return SuperHumanos(**kwargs)
        