import unittest
from pandabook import Panda
from pandabook import PandaSocialNetwork


class PandaTest(unittest.TestCase):
    def setUp(self):
        self.panda = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_create_panda(self):
        self.assertTrue(isinstance(self.panda, Panda))

    def test_raises_eroro_value(self):
        with self.assertRaises(ValueError):
            pan = Panda("DIdi", "plok", "female")

    def test_raises_error_create_email(self):
        with self.assertRaises(TypeError):
            pan = Panda("sda", 1, "da")

    def test_raises_error_create_gender(self):
        with self.assertRaises(ValueError):
            pan = Panda("ivo", "email@mail.com", 33)

    def test_dunder__eq__(self):
        panda2 = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(self.panda, panda2)

    def test_name_eq(self):
        self.assertEqual(self.panda.name(), "Ivo")

    def test_email_eq(self):
        self.assertEqual(self.panda.email(), "ivo@pandamail.com")

    def test_gender_eq(self):
        self.assertEqual(self.panda.gender(), "male")

    def test_isMale(self):
        self.assertTrue(self.panda.isMale())

    def test_isFemale(self):
        self.assertFalse(self.panda.isFemale())

    def test_str_panda(self):
        self.assertEqual(str(self.panda), "Ivo")

    def test_kunfopanda_in_dict(self):
        pandas = {}
        kunfo_panda = Panda("Kunfo", "kunfo_nidja@niodjmial.jaba", "female")
        kiro_panda = Panda("kiro", "Kiro_ubiecanapandi@unisofia.fmi", "male")
        pandas[kunfo_panda] = 1
        pandas[kiro_panda] = 100000
        self.assertEqual(pandas, {kiro_panda: 100000, kunfo_panda: 1})


class PandaSocialNetworkTest(unittest.TestCase):
    def setUp(self):
        self.pandabook = PandaSocialNetwork()
        self.kiro_panda = Panda("kiro", "Kiro_ubiecanapandi@unisofia.fmi", "male")
        self.kunfo_panda = Panda("Kunfo", "kunfo_nidja@niodjmial.jaba", "female")
        self.dubai_panda = Panda("Azi", "azi@ehmaa.asd", "male")

    def test_create_panda_book(self):
        self.assertTrue(isinstance(self.pandabook, PandaSocialNetwork))

    def test_create_panda_empty_dict(self):
        self.assertEqual(self.pandabook.pandas, {})

    def test_addind_panda(self):
        kiro_panda = Panda("kiro", "Kiro_ubiecanapandi@unisofia.fmi", "male")
        self.pandabook.add_panda(kiro_panda)
        self.assertEqual(self.pandabook.pandas, {kiro_panda: []})

    def test_raises_exception(self):
        with self.assertRaises(Exception):
            kiro_panda = Panda("kiro", "Kiro_ubiecanapandi@unisofia.fmi", "male")
            self.pandabook.add_panda(kiro_panda)
            self.pandabook.add_panda(kiro_panda)

    def test_has_panda_in_pandabooK(self):
        kiro_panda = Panda("kiro", "Kiro_ubiecanapandi@unisofia.fmi", "male")
        self.pandabook.add_panda(kiro_panda)
        self.assertTrue(self.pandabook.has_panda(kiro_panda))

    def test_has_not_panda_in_pandabook(self):
        kiro_panda = Panda("kiro", "Kiro_ubiecanapandi@unisofia.fmi", "male")
        self.pandabook.add_panda(kiro_panda)
        kunfo_panda = Panda("Kunfo", "kunfo_nidja@niodjmial.jaba", "female")
        self.assertFalse(self.pandabook.has_panda(kunfo_panda))

    def test_are_friends(self):
        self.pandabook.add_panda(self.kiro_panda)
        self.pandabook.add_panda(self.kunfo_panda)
        self.assertFalse(self.pandabook.are_friends(self.kiro_panda, self.kunfo_panda))

    def test_make_friends(self):
        self.pandabook.add_panda(self.kunfo_panda)
        self.pandabook.add_panda(self.kiro_panda)
        self.pandabook.make_friends(self.kunfo_panda, self.kiro_panda)
        self.assertEqual(self.pandabook.pandas[self.kiro_panda], [self.kunfo_panda])

    def test_friends_of(self):
        self.pandabook.add_panda(self.kunfo_panda)
        self.pandabook.add_panda(self.kiro_panda)
        self.pandabook.make_friends(self.kunfo_panda, self.kiro_panda)
        self.assertEqual(self.pandabook.friends_of(self.kiro_panda), [self.kunfo_panda])

    def test_friends_of_with_non_member_panda(self):
        self.pandabook.add_panda(self.kunfo_panda)
        self.pandabook.add_panda(self.kiro_panda)
        self.pandabook.make_friends(self.kunfo_panda, self.kiro_panda)
        hashPanda = Panda("Smokin_panda", "smoke_man@abv.bg", "female")
        self.assertFalse(self.pandabook.friends_of(hashPanda))

    def test_how_many_genders_in_network(self):
        self.pandabook.add_panda(self.kunfo_panda)
        self.assertEqual(self.pandabook.how_many_gender_in_network(1, self.kunfo_panda, "female"), 0)

    def test_how_many_genders_in_network_3pandas(self):
        self.pandabook.add_panda(self.kunfo_panda)
        self.pandabook.add_panda(self.dubai_panda)
        self.pandabook.make_friends(self.kunfo_panda, self.dubai_panda)
        self.pandabook.add_panda(self.kiro_panda)
        self.pandabook.make_friends(self.dubai_panda, self.kiro_panda)
        self.assertEqual(self.pandabook.how_many_gender_in_network(2, self.kunfo_panda, "male"), 2)

    def test_pandabook_file_extraction(self):
        self.pandabook.add_panda(self.kunfo_panda)
        self.pandabook.add_panda(self.dubai_panda)
        self.pandabook.make_friends(self.kunfo_panda, self.dubai_panda)
        self.pandabook.add_panda(self.kiro_panda)
        self.pandabook.make_friends(self.dubai_panda, self.kiro_panda)
        self.pandabook.write_to_file("pandabook.json")
        x = self.pandabook.pandas
        self.pandabook.read_from_file("pandabook.json")
        self.assertEqual(x, self.pandabook.pandas)

if __name__ == '__main__':
    unittest.main()
