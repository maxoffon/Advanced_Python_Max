import unittest
from urllib.parse import unquote
from ex2 import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()

    def test_timeout_expired(self):
        data = self.app.post('/runcode', data={"code": "print(8)", "timeout": 0})
        new_data = unquote(data.get_data(as_text=True))
        self.assertTrue("killed by timeout: True" in new_data)

    def test_incorrect_input(self):
        data = self.app.post('/runcode', data={"code": "print(8)k", "timeout": 10})
        new_data = unquote(data.get_data(as_text=True))
        self.assertEqual(400, data.status_code)
        self.assertTrue("Некорректный ввод" in new_data)

    def test_correct(self):
        data = self.app.post('/runcode', data={"code": "print(8)", "timeout": 10})
        new_data = unquote(data.get_data(as_text=True))
        self.assertEqual(200, data.status_code)
        self.assertTrue('stdout: 8' in new_data)

    def test_code_required(self):
        data = self.app.post('/runcode', data={"timeout": 10})
        new_data = unquote(data.get_data(as_text=True))
        self.assertEqual(400, data.status_code)
        self.assertTrue('Обязательно введите исполняемый код' in new_data)
