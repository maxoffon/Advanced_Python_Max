import unittest
from datetime import datetime
from mod2.fourth import app
from freezegun import freeze_time
import re


class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username_with_weekday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    date = "2023-03-14"
    @freeze_time(date)
    def test_correct_weekday(self):
        username = 'макс'
        weekdays = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
        day = weekdays[datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        resp_user = re.split('[.!]', response_text)[0].split().pop()
        self.assertFalse(resp_user in weekdays)
        self.assertTrue(day in response_text)
