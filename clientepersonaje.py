from personajesfactory import AbstractPersonajeFactory

class clientePersonaje():
    __factory: AbstractPersonajeFactory
    def addpersonajefactory(self, factory: AbstractPersonajeFactory, **kwargs):
        self.__factory = factory
        return self.__factory.createPersonaje(**kwargs)