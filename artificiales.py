from personajes import Personajes


class Artificial(Personajes):
    _laboratory: str

    def __init__(
            self, **kwargs
    ):
        super().__init__(**kwargs)
        self._laboratory = kwargs['laboratory']

    @property
    def laboratory(self) -> str:
        return self._laboratory

    @laboratory.setter
    def galaxy(self, laboratory: str) -> None:
        self._laboratory=laboratory
