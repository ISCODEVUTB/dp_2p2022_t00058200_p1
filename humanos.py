from personajes import Personajes


class Humanos(Personajes):
    _birth_continent: str
    _country: str

    # contructor de la clase
    def __init__(self, name: str, age: int, sex: str, description: str, birth_continent: str, country: str):
        self._birth_continent = birth_continent
        self._country = country
        super().__init__(name, age, sex, description)

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


