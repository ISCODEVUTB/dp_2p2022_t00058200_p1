import unittest
from  superHumanos import SuperHumanos
from humanos import Humanos
from alienz import  Alienz
from artificiales import  Artificial
from poderes import Poderes
from habilidades import  Habilidades
from poderes import  Poderes
from armas import Armas
from personalidades import  Personalidades
from debilidades import  Debilidades

class CodeTest(unittest.TestCase):
    def test_personaje_humano(self):
        humano = Humanos('test1', 12, 'male', 'una breve descripcio', 'america', 'argentins')
        poder = Poderes('poder', 'volar', '100')
        humano.league('marvel')

        humano.add(poder)
        self.assertEqual(humano.liga, 'marvel')
        self.assertEqual(humano.age, 12)

    def testTrue(self):
        humano = Humanos('test1', 12, 'male', 'una breve descripcio', 'america', 'argentins')
        poder = Poderes('poder', 'volar', '100')
        self.assertTrue(humano.add(poder))

    def testInA(self):
        humano = Humanos('test2', 12, 'male', 'una breve descripcio', 'america', 'argentins')
        poder = Poderes('poder_1', 'volar', '100')
        humano.league('marvel')
        humano.add(poder)
        self.assertIn(poder, humano.characterizations)

    def testIs(self):
        humano1 = Humanos('test3', 12, 'male', 'una breve descripcio', 'america', 'argentins')
        poder_1 = Poderes('poder_2', 'volar', '100')
        humano1.league('marvel')
        humano1.add(poder_1)
        print(humano1.characterizations)
        self.assertIn(poder_1, humano1.characterizations)

    def test_none(self):
        humano_1 = Humanos('test4', 12, 'male', 'una breve descripcio', 'america', 'argentins')
        self.assertIsNone(humano_1.liga)

    def test_personaje_aliens(self):
        alien2 = Alienz('wert', 300, 'male', 'viajador de galaxia', 'andromeda')
        habilidad1 = Habilidades('habilidad', 'relacionarse con humanos')
        alien2.add(habilidad1)
        # self.assertEqual(alien2.characterizations[0].name_caraterizacion,'habilidad')
        self.assertEqual(alien2.description, 'viajador de galaxia')

    def test_none_1(self):
        alien = Alienz('wert', 300, 'male', 'viajador de galaxia', 'andromeda')
        habilidad = Habilidades('habilidad', 'relacionarse con humanos')
        alien.add(habilidad)
        assert alien.characterizations is not None

    def test_fast(self):
        alien = Alienz('flash', 300, 'male', 'viajador de galaxia 1', 'andromeda')
        habilidad = Habilidades('habilidad', 'relacionarse con humanos')
        alien.add(habilidad)
        self.assertEqual(alien.name, 'flash')


    def test_poder(self):
        poder = Poderes('poder', 'invisible', 12)
        habilidad = Habilidades('habilidad', 'tratar bien')
        self.assertEqual(poder.name_power, 'invisible')

    def test_habilidad(self):
        habi = Habilidades('habilidad', 'tratar_personas')
        self.assertEqual(habi.name_ability, 'tratar_personas')

    def test_getter(self):
        super_humano = SuperHumanos('goku', 12, 'f', 'goku es el mejor', 200, 'america', 'colombia')
        self.assertEqual(super_humano.name, 'goku')

    def other_test_getter(self):
        artificial = Artificial('roboco', 100, 'm', 'roboco is a robo', 'timers')
        self.assertIsInstance(artificial, Artificial)

    def test_setter(self):
        super_humano_a = SuperHumanos('goku', 12, 'f', 'goku es el mejor', 200, 'america', 'colombia')
        super_humano_a.name = 'gian'
        self.assertEqual(super_humano_a.name, 'gian')
    def test_artificial(self):
        artificial = Artificial('roco',100,'m','roboco is to','tm')
        self.assertEqual(artificial.name,'roco')
    def test_set(self):
        artificial = Artificial('roco', 100, 'm', 'roboco is to', 'tm')
        artificial.name = 'ROBOCO'
        self.assertEqual(artificial.name, 'ROBOCO')
    def test_armas(self):
        armas = Armas('metralleta','mp5',100,'negra')
        armas.color = 'gray'
        self.assertNotIn('negra',armas.color)
    def test_armas_2(self):
        armas = Armas('metralleta','mp5',100,'negra')
        armas.color = 'gray'
        self.assertEqual('gray',armas.color)
    def test_personalid(self):
        p = Personalidades('personalidad','alegre')
        self.assertEqual(p.name_personalities,'alegre')
    def test_debilidad(self):
        deb = Debilidades('debilidad','llorar')
        self.assertEqual(deb.name_weakness,'llorar')

    def test_artificiales(self):
        art =Artificial('art',400,'f','artificoa','bell')
        self.assertIsInstance(art,Artificial)