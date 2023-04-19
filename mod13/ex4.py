"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3

SOVIN_SALARY = 100000

request = """
UPDATE table_effective_manager
SET salary = ROUND(salary * 1.1)
WHERE name = ? AND NOT name LIKE 'Иван Совин'
"""
request_delete = """
DELETE
FROM table_effective_manager
WHERE salary >= ? AND NOT name LIKE 'Иван Совин'
"""

def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    c.execute(request, (name, ))
    c.execute(request_delete, (SOVIN_SALARY, ))

with sqlite3.connect('hw.db') as conn:
    c = conn.cursor()
    ivan_sovin_the_most_effective(c, 'Соколова И.Е.')


