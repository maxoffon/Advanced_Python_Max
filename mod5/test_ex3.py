import unittest
from ex3 import BlockErrors


class MyTestCase(unittest.TestCase):
    def test_ignoring_errors(self):
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / 0
        self.assert_(True)

    def test_unexpected_error(self):
        err_types = {ZeroDivisionError}
        with self.assertRaises(TypeError):
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')

    def test_skip_inner_error(self):
        outer_err_types = {TypeError}
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            with BlockErrors(inner_err_types):
                a = 1 / '0'
            print('Внутренний блок: выполнено без ошибок')
        print('Внешний блок: выполнено без ошибок')
        self.assert_(True)

    def test_daughter_errors(self):
        err_types = {Exception}
        with BlockErrors(err_types):
            a = 1 / '0'
        print('Выполнено без ошибок')
        self.assert_(True)