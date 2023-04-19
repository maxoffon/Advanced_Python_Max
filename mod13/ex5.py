"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""
import sqlite3

request_teams = """
INSERT INTO uefa_commands
VALUES (?,?,?,?)
"""

request_draw = """
INSERT INTO uefa_draw (command_number, group_number)
VALUES (?,?)
"""

def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    teams_names = [f'team {i + 1}' for i in range(number_of_groups * 4)]
    teams_countries = [f'country {i + 1}' for i in range(number_of_groups * 4)]
    levels = ['strong'] * number_of_groups + ['average'] * 2 * number_of_groups + ['weak'] * number_of_groups
    res = [(i + 1, teams_names[i], teams_countries[i], levels[i]) for i in range(number_of_groups * 4)]
    c.executemany(request_teams, res)

    res2 = []
    for i in range(number_of_groups):
        res2 += [(res[i][0], i + 1),
                 (res[2*i + number_of_groups][0], i + 1),
                 (res[2*i + number_of_groups + 1][0], i + 1),
                 (res[i + (number_of_groups - 1) * number_of_groups][0], i + 1)]
    c.executemany(request_draw, res2)


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as conn:
        c = conn.cursor()
        generate_test_data(c, 4)