from caracterizacion import Caracterizacion


class Poderes(Caracterizacion):

    _name_power: str
    _level_power: str

    def __init__(self, name: str, name_power: str, level_power: str):
        super().__init__(name)
        self._level_power = level_power
        self._name_power = name_power

    @property
    def level_power(self) -> str:
        return self._level_power

    @level_power.setter
    def level_power(self, level_power: str ) -> None:
        self._level_power = level_power

    @property
    def name_power(self) -> str:
        return self._name_power

    @name_power.setter
    def name_power(self, name_power: str) -> None:
        self._name_power = name_power
