from mod3.fourth import Person
import unittest
from datetime import datetime

class TestClassPerson(unittest.TestCase):
    def test_init(self):
        example_with_street = Person('Max', 2004, 'Groove Str.')
        example_with_no_street = Person('Jake', 2000)
        self.assertEqual('Max', example_with_street.name)
        self.assertEqual(2004, example_with_street.yob)
        self.assertEqual('Groove Str.', example_with_street.address)
        self.assertEqual('Jake', example_with_no_street.name)
        self.assertEqual(2000, example_with_no_street.yob)
        self.assertEqual('', example_with_no_street.address)

    def test_get_age(self):
        ex = Person('Max', 2004, 'Groove Str.')
        self.assertEqual(datetime.now().year - 2004, ex.get_age())

    def test_get_name(self):
        ex = Person('Max', 2004, 'Groove Str.')
        self.assertEqual('Max', ex.get_name())

    def test_set_name(self):
        ex = Person('Max', 2004, 'Groove Str.')
        new_name = 'Jake'
        ex.set_name(new_name)
        self.assertEqual(new_name, ex.get_name())

    def test_set_address(self):
        ex = Person('Max', 2004, 'Groove Str.')
        new_address = 'St. Louis Avn'
        ex.set_address(new_address)
        self.assertEqual(new_address, ex.get_address())

    def test_get_address(self):
        ex = Person('Max', 2004, 'Groove Str.')
        self.assertEqual('Groove Str.', ex.get_address())

    def test_is_homeless(self):
        ex_with_home = Person('Max', 2004, 'Groove Str.')
        ex_with_no_home = Person('Max', 2004)
        self.assertTrue(ex_with_no_home.is_homeless())
        self.assertFalse(ex_with_home.is_homeless())