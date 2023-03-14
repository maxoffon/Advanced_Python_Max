import unittest


def decrypt(code):
    list_code = list(code)
    result = []
    dot_flag = False
    for i in range(len(list_code)):
        if list_code[i] != '.':
            result.append(list_code[i])
        else:
            if not dot_flag:
                dot_flag = True
            else:
                if len(result) > 0:
                    result.pop()
                dot_flag = False
    return ''.join(result)


class TestDecryptor(unittest.TestCase):
    def test_no_other_symbols_but_dots(self):
        code = '.'
        self.assertEqual('', decrypt(code))

    def test_one_dot_in_a_code(self):
        code = 'абра-кадабра.'
        self.assertEqual('абра-кадабра', decrypt(code))

    def test_two_dots_in_a_code(self):
        codes = ['абраа..-кадабра', 'абра--..кадабра']
        [self.assertEqual('абра-кадабра', decrypt(item)) for item in codes]

    def test_two_dots_and_one_dot_separetely(self):
        codes = ['абраа..-.кадабра', '1..2.3']
        ans = ['абра-кадабра', '23']
        [self.assertEqual(ans[i], decrypt(codes[i])) for i in range(len(codes))]

    def test_more_than_two_dots(self):
        codes = ['абрау...-кадабра', 'абра........', 'абр......а.', '1.......................']
        ans = ['абра-кадабра', '', 'а', '']
        [self.assertEqual(ans[i], decrypt(codes[i])) for i in range(len(codes))]