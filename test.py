import unittest
from clientepersonaje import clientePersonaje
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
from factorysuperhumanos import  FactorySuperHumanos
from factoryhumanos import FactoryHumanos
from factoryalienz import FactoryAlienz
from factoryartificiales import FactoryArtificial

class CodeTest(unittest.TestCase):
    humano_dict = {'name':'test1','age': 12,'sex': 'male','description': 'una breve descripcio','birth_continent': 'america','country': 'argentins'}
    humano1_dict = {'name':'test2','age': 12,'sex': 'male','description': 'una breve descripcio','birth_continent': 'america','country': 'argentins'}
    humano2_dict = {'name':'test3','age': 12,'sex': 'male','description': 'una breve descripcio','birth_continent': 'america','country': 'argentins'}



    def test_personaje_humano(self):
        humano = Humanos(**self.humano_dict)
        poder = Poderes('poder', 'volar', '100')
        humano.league('marvel')
        print(humano.age)
        humano.add(poder)
        self.assertEqual(humano.liga, 'marvel')
        self.assertEqual(humano.age, 12)

    def testTrue(self):
        humano = Humanos(**self.humano_dict)
        poder = Poderes('poder', 'volar', '100')
        self.assertTrue(humano.add(poder))

    def testInA(self):
        humano = Humanos(**self.humano_dict)
        poder = Poderes('poder_1', 'volar', '100')
        humano.league('marvel')
        humano.add(poder)
        self.assertIn(poder, humano.characterizations)

    def testIs(self):
        humano1 = Humanos(**self.humano1_dict)
        poder_1 = Poderes('poder_2', 'volar', '100')
        humano1.league('marvel')
        humano1.add(poder_1)
        print(humano1.characterizations)
        self.assertIn(poder_1, humano1.characterizations)

    def test_none(self):
        humano_1 = Humanos(**self.humano2_dict)
        self.assertIsNone(humano_1.liga)

    alien_1 = {'name':'wert', 'age': 300, 'sex': 'male', 'description':'viajador de galaxia', 'galaxy':'andromeda'}
    def test_personaje_aliens(self):
        alien2 = Alienz(**self.alien_1)
        habilidad1 = Habilidades('habilidad', 'relacionarse con humanos')
        alien2.add(habilidad1)
        # self.assertEqual(alien2.characterizations[0].name_caraterizacion,'habilidad')
        self.assertEqual(alien2.description, 'viajador de galaxia')
    alien_2 = {'name':'wert', 'age': 300, 'sex': 'male', 'description':'viajador de galaxia', 'galaxy':'andromeda'}
    def test_none_1(self):
        alien = Alienz(**self.alien_2)
        habilidad = Habilidades('habilidad', 'relacionarse con humanos')
        alien.add(habilidad)
        assert alien.characterizations is not None
    alien_3 = {'name':'flash', 'age': 300, 'sex': 'male', 'description':'viajador de galaxia', 'galaxy':'andromeda'}
    def test_fast(self):
        alien = Alienz(**self.alien_3)
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

    sh_1 = {'name':'goku','age': 12,'sex': 'f','description': 'goku es el mejor','time_life':'no se','birth_continent': 'america','country': 'colombia'}
    def test_getter(self):
        super_humano = SuperHumanos(**self.sh_1)
        self.assertEqual(super_humano.name, 'goku')

    art_1 = {'name':'roboco','age': 100,'sex': 'male','description': 'roboco is a robo','laboratory': 'timers'}
    def other_test_getter(self):
        artificial = Artificial(**self.art_1)
        self.assertIsInstance(artificial, Artificial)

    def test_setter(self):
        super_humano_a = SuperHumanos(**self.sh_1)
        super_humano_a.name = 'gian'
        self.assertEqual(super_humano_a.name, 'gian')

    art_2 = {'name':'roco','age': 100,'sex': 'male','description': 'roboco is to','laboratory': 'tm'}
    def test_artificial(self):
        artificial = Artificial(**self.art_2)
        self.assertEqual(artificial.name,'roco')
    def test_set(self):
        artificial = Artificial(**self.art_2)
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
    art_3 = {'name':'art','age': 400,'sex': 'f','description': 'artificoa','laboratory': 'bell'}

    def test_factory(self):
        cliente = clientePersonaje()
        super_humano = cliente.addpersonajefactory(FactorySuperHumanos(),**self.sh_1)
        self.assertIsInstance(super_humano,SuperHumanos)


if __name__ == '__main__':
    unittest.main()