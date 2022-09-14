from personajes import Personajes


class Artificial(Personajes):
    _laboratory: str

    def __init__(
            self, name: str, age: int, sex: str, description: str, laboratory: str
    ):
        super().__init__(name, age, sex, description)
        self._laboratory = laboratory

    @property
    def laboratory(self) -> str:
        return self._laboratory

    @laboratory.setter
    def galaxy(self, laboratory: str) -> None:
        self._laboratory=laboratory
