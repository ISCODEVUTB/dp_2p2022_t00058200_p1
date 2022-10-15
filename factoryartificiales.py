from personajesfactory import AbstractPersonajeFactory

from artificiales import Artificial

class FactoryArtificial(AbstractPersonajeFactory):

    def createPersonaje(self,**kwargs):

        return Artificial(**kwargs)