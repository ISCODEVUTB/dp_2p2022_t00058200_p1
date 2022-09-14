from personajes import Personajes
class Alienz(Personajes):
    _galaxy: str

    def __init__(
            self, name: str, age: int, sex: str, description: str, galaxy: str
    ):
        super().__init__(name, age, sex, description)
        self._galaxy = galaxy
    @property
    def galaxy(self) -> str:
        return self._galaxy

    @galaxy.setter
    def galaxy(self, galaxy: str) -> None:
        self._galaxy = galaxy
