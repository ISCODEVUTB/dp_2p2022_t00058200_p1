from personajes import Personajes
class Alienz(Personajes):
    _galaxy: str

    def __init__(
            self, **kwargs
    ):
        super().__init__(**kwargs)
        self._galaxy = kwargs['galaxy']
    @property
    def galaxy(self) -> str:
        return self._galaxy

    @galaxy.setter
    def galaxy(self, galaxy: str) -> None:
        self._galaxy = galaxy
