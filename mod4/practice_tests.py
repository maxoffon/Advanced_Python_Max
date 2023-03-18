import unittest
from urllib.parse import unquote
from mod4.practice import app


class Test(unittest.TestCase):
    def setUp(self):
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()

    def testRequiredName(self):
        data = self.app.post('/registration', data={"email": "ar@mail.ru",
                                                      "phone": 9501936612,
                                                      "address": "aaa"})
        new_data = unquote(data.get_data(as_text=True))
        print(new_data)
        self.assertEqual(400, data.status_code)
        self.assertTrue("'name': ['This field is required.']" in new_data)

    def testRequiredAddress(self):
        data = self.app.post('/registration', data={"email": "ar@mail.ru",
                                                      "phone": 9501936612,
                                                      "name": "aaa"})
        new_data = unquote(data.get_data(as_text=True))
        print(new_data)
        self.assertEqual(400, data.status_code)
        self.assertTrue("'address': ['This field is required.']" in new_data)

    def testRequiredPhone(self):
        data = self.app.post('/registration', data={"email": "ar@mail.ru",
                                                      "name": '9501936612',
                                                      "address": "aaa"})
        new_data = unquote(data.get_data(as_text=True))
        print(new_data)
        self.assertEqual(400, data.status_code)
        self.assertTrue("'phone': ['This field is required.']" in new_data)




