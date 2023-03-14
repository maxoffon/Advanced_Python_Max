# Ошибки файла fourth.py #
1. NameError: name 'datetime' is not defined <br>
Test: *test_get_age* <br>
Не определена библиотека datetime (используйте import)
***
2. NameError: name 'address' is not defined <br>
Test: *test_is_homeless* <br>
Нет локальной переменной address в зоне видимости (возможно, вы имели в виду self.address)
***
3. AssertionError: 'St. Louis Avn' != 'Groove Str.' <br>
Test: *test_set_address* <br>
Неккоректное присваивание (используйте одиночный символ '=')
***
4. AssertionError: 'Jake' != 'Max' <br>
Test: *test_set_name* <br>
Присваивание не имеет эффекта (неиспользуемый переданный параметр name)