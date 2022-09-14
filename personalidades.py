from caracterizacion import Caracterizacion


class Personalidades(Caracterizacion):
    _nane_weakness: str

    def __init__(self, name: str, name_personalities: str):
        super().__init__(name)
        self._nane_weakness = name_personalities

    @property
    def name_personalities(self) -> str:
        return self._nane_weakness

    @name_personalities.setter
    def name_personalities(self, name_personalities: str) -> None:
        self._nane_weakness = name_personalities


