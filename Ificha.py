from abc import ABCMeta, abstractmethod


class IFicha(metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def league(self):
        pass

    @abstractmethod
    def enemy(self):
        pass
