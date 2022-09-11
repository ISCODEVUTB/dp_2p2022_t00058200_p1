import unittest
from  superHumanos import SuperHumanos
from humanos import Humanos
from alienz import  Alienz
from poderes import Poderes
from habilidades import  Habilidades
class Personajes(unittest.TestCase):

    def test_personaje_humano(self):

        humano = Humanos('test1', 12, 'male', 'una breve descripcio', 'america', 'argentins')
        poder = Poderes('poder','volar','100')
        humano.league('marvel')
        humano.add(poder)
        self.assertEqual(humano.liga,'marvel')
        self.assertEqual(humano.age,12)
        self.assertEqual(humano.characterizations[0],poder)

class OtroTest(unittest.TestCase):

    def test_personaje_aliens(self):

        alien = Alienz('wert',300,'male','viajador de galaxia','andromeda')
        habilidad = Habilidades('habilidad','relacionarse con humanos')
        alien.add(habilidad)
        self.assertEqual(alien.characterizations[0],habilidad)
        self.assertEqual(alien.description,'viajador de galaxia')

