from personajes import Personajes


class Humanos(Personajes):
    _birth_continent: str
    _country: str

    # contructor de la clase
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._birth_continent = kwargs['birth_continent']
        self._country = kwargs['country']

    @property
    def birth_continent(self) -> str:
        return self._birth_continent

    @birth_continent.setter
    def birth_continent(self, birth_continent: str) -> None:
        self._birth_continent = birth_continent

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        self._country = country


