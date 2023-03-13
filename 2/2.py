import sys


def get_mean_size(data_lines):
    if len(data_lines) == 0:
        return 'Нет файлов'
    result = 0
    for line in data_lines:
        a = line.split()[4]
        try:
            result += int(a)
        except ValueError:
            return 'Невозможно посчитать среднее значение'
    return f'Средний размер файла: {str(round(result / len(data_lines), 2))} байт'


data = sys.stdin.readlines()[1:]
print(get_mean_size(data))
