from personajesfactory import AbstractPersonajeFactory


from alienz import Alienz

class FactoryAlienz(AbstractPersonajeFactory):

    def createPersonaje(self, **kwargs):
        return Alienz(**kwargs)