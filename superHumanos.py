from personajes import Personajes


class SuperHumanos(Personajes):
    _time_of_life: str
    _birth_continent: str
    _country: str

    def __init__(
            self, name: str, age: int, sex: str, description: str, time_life: str, birth_continent: str, country: str
    ):
        super().__init__(name, age, sex, description)
        self._time_of_life = time_life
        self._country = country
        self._birth_continent = birth_continent

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

    @property
    def time_life(self) -> str:
        return self._time_of_life

    @time_life.setter
    def time_life(self, time_life: str) -> None:
        self._country = time_life
