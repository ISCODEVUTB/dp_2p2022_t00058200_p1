from caracterizacion import Caracterizacion


class Armas(Caracterizacion):
    _name_weapons: str
    _number_munnition: int
    _color: str

    def __init__(self, name: str, nombre_arma: str, numero_municiones: int, color:str):
        super().__init__(name)
        self._name_weapons = nombre_arma
        self._number_munnition = numero_municiones
        self._color = color

    @property
    def name_weapons(self) -> str:
        return self._name_weapons

    @name_weapons.setter
    def name_weapons(self, name_weapons: str) -> None:
        self._name_weapons = name_weapons

    @property
    def number_munnitions(self) -> str:
        return self._number_munnition

    @number_munnitions.setter
    def number_munnitions(self, number_munnitions: int) -> None:
        self._number_munnition = number_munnitions

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        self._color = color
