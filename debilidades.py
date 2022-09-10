from caracterizacion import Caracterizacion


class Debilidades(Caracterizacion):
    _nane_weakness: str

    def __init__(self, name: str, name_weakness: str):
        super().__init__(name)
        self._nane_weakness = name_weakness

    @property
    def name_weakness(self) -> str:
        return self._nane_weakness

    @name_weakness.setter
    def name_weakness(self, name_weakness: str) -> None:
        self._nane_weakness = name_weakness


