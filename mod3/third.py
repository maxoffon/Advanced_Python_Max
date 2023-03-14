import unittest
from mod2.seventh import app, storage


def full_storage(new_dict: dict):
    for key, value in new_dict.items():
        storage[key] = value


class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.test_storage = {'2022': [{'11': 1000, '12': 2000}, 3000], '2021': [{'09': 100, '10': 200}, 300]}
        full_storage(self.test_storage)

    def test_add_correct(self):
        date = '20221210'
        date_format = '10.12.2022'
        amount = 1000
        response = self.app.get('/add/' + '/'.join((date, str(amount))))
        response_text = response.data.decode()
        self.assertTrue(date_format in response_text and str(amount) in response_text)

    def test_add_incorrect(self):
        date = '20251338'
        amount = 2000
        response = self.app.get('/add/' + '/'.join((date, str(amount))))
        response_text = response.data.decode()
        self.assertEqual('Некорректная дата', response_text)

    def test_add_wrong_format(self):
        date = '12321234f'
        amount = 100
        with self.assertRaises(ValueError):
            self.app.get('/add/' + '/'.join((date, str(amount))))

    def test_calculate_year(self):
        year = '2022'
        response = self.app.get('/calculate/' + year)
        response_text = response.data.decode()
        correct_sum = 3000
        self.assertEqual(correct_sum, int(response_text.split().pop()))

    def test_calculate_year_empty_storage(self):
        storage.clear()
        year = '2022'
        response = self.app.get('/calculate/' + year)
        response_text = response.data.decode()
        correct_sum = 0
        self.assertEqual(correct_sum, int(response_text.split().pop()))

    def test_calculate_year_when_no_year_in_storage(self):
        year = '1900'
        response = self.app.get('/calculate/' + year)
        response_text = response.data.decode()
        correct_sum = 0
        self.assertEqual(correct_sum, int(response_text.split().pop()))

    def test_calculate_year_month(self):
        year = '2022'
        month = '12'
        response = self.app.get('/calculate/' + '/'.join((year, month)))
        response_text = response.data.decode()
        correct_year_sum = 3000
        correct_month_sum = 2000
        self.assertEqual(correct_year_sum, int(response_text.split(',')[0].split().pop()))
        self.assertEqual(correct_month_sum, int(response_text.split(',')[1].split().pop()))

    def test_calculate_year_month_empty_storage(self):
        storage.clear()
        year = '2022'
        month = '12'
        response = self.app.get('/calculate/' + '/'.join((year, month)))
        response_text = response.data.decode()
        correct_year_sum = 0
        correct_month_sum = 0
        self.assertEqual(correct_year_sum, int(response_text.split(',')[0].split().pop()))
        self.assertEqual(correct_month_sum, int(response_text.split(',')[1].split().pop()))

    def test_calculate_year_month_when_no_date_in_storage(self):
        year = '1900'
        month = '01'
        response = self.app.get('/calculate/' + '/'.join((year, month)))
        response_text = response.data.decode()
        correct_year_sum = 0
        correct_month_sum = 0
        self.assertEqual(correct_year_sum, int(response_text.split(',')[0].split().pop()))
        self.assertEqual(correct_month_sum, int(response_text.split(',')[1].split().pop()))

