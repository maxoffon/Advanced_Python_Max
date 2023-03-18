import json
import unittest
from mod4.ex1_2 import app


class Test(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.dataset = {'email': 'al@mail.ru',
                        'phone': '1000000000',
                        'phone2': '9999999999',
                        'name': 'Max',
                        'address': 'Wherever',
                        'index': '620102',
                        'comment': 'Something'}

    def testNoFieldsProvided(self):
        data = self.app.post('/registration')
        error_data = json.loads(data.get_data(as_text=True).replace("'", '"').split('Incorrect input: ')[1])
        self.assertEqual(400, data.status_code)
        for item in ['email', 'phone', 'phone2', 'name', 'address', 'index']:
            self.assertTrue(item in error_data)
            self.assertTrue('Обязательное поле для заполнения' in error_data[item])

    def testAllFieldsCorrect(self):
        data = self.app.post('/registration', data=self.dataset)
        self.assertEqual(200, data.status_code)
        self.assertEqual(f'User Max successfully registered!', data.get_data(as_text=True))

    def testIncorrectEmail(self):
        self.dataset['email'] = 'al111.com'
        data = self.app.post('/registration', data=self.dataset)
        self.assertEqual(400, data.status_code)
        self.assertTrue('Неверный формат email' in data.get_data(as_text=True))

    def testWrongIntegerFormatPhone(self):
        self.dataset['phone'] = '1f'
        data = self.app.post('/registration', data=self.dataset)
        self.assertTrue('Not a valid integer value' in data.get_data(as_text=True))

    def testWrongIntegerFormatPhone2(self):
        self.dataset['phone2'] = '1f'
        data = self.app.post('/registration', data=self.dataset)
        self.assertTrue('Not a valid integer value' in data.get_data(as_text=True))

    def testWrongIntegerFormatIndex(self):
        self.dataset['index'] = 's'
        data = self.app.post('/registration', data=self.dataset)
        self.assertTrue('Not a valid integer value' in data.get_data(as_text=True))
