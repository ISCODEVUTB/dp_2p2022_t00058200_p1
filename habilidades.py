from caracterizacion import Caracterizacion


class Habilidades(Caracterizacion):
    _nane_ability: str

    def __init__(self, name: str, name_ability: str):
        super().__init__(name)
        self._nane_ability = name_ability

    @property
    def name_ability(self) -> str:
        return self._nane_ability

    @name_ability.setter
    def name_ability(self, name_ability: str) -> None:
        self._nane_ability = name_ability


