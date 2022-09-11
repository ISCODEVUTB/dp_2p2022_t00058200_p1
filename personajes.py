"""
author : Gian franco valdiris Cerpa
"""
from abc import ABC
from Ificha import IFicha
from caracterizacion import Caracterizacion
from typing import List
# abstrac class personajes


class Personajes(ABC, IFicha):
    _name: str
    _age: int
    _sex: str
    _description: str
    _league: str
    _enemy: list = []
    _characterizations = []

    def __init__(self, name: str, age: int, sex: str, description: str):
        self._name = name
        self._description = description
        self._age = age
        self._sex = sex

    # setters and getters methods

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def sex(self) -> str:
        return self._sex

    @property
    def description(self) -> str:
        return self._description

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @age.setter
    def age(self, age:int ) -> None:
        self._age = age

    @sex.setter
    def sex(self, sex: str) -> None:
        self._sex = sex

    @description.setter
    def description(self, des: str) -> None:
        self._description = des

    # methods of interface Ificha

    def league(self, liga: str):
        self._league = liga

    @property
    def liga(self) -> str:
        return self._league

    def add(self, caracterizacion: Caracterizacion):
        self._characterizations.append(caracterizacion)
        print('se añadio la caracterizacion al personaje')

    def enemy(self, personaje):
        self._enemy.append(personaje)

    @property
    def characterizations(self):
        return self._characterizations
    def to_string(self):
        print('''
            nombre :{}
            sexo : {}
            edad : {}
            descripcion : {}
        '''.format(self._name, self._sex, self._age, self._description))
