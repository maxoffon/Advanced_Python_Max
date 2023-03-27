import datetime
import unittest
import json
import ex3


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = ex3.logger
        self.f = open('skillbox_json_messages.log', 'r', encoding='utf-8')

    def test_json_no_quotes(self):
        self.logger.info('Message')
        dictionary = {"time": f"{datetime.datetime.now().strftime('%H:%M:%S')}",
                      "level": "INFO",
                      "message": "Message"}
        string = json.dumps(dictionary)
        self.assertTrue(string in [item.replace('\n', '') for item in self.f.readlines()])

    def test_json_double_quotes(self):
        self.logger.info('"')
        dictionary = {"time": f"{datetime.datetime.now().strftime('%H:%M:%S')}",
                      "level": "INFO",
                      "message": "\""}
        string = json.dumps(dictionary)
        self.assertTrue(string in [item.replace('\n', '') for item in self.f.readlines()])

    def tearDown(self):
        self.f.close()


if __name__ == '__main__':
    unittest.main()
