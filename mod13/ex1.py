"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3

sql_request = """
SELECT * 
FROM table_truck_with_vaccine
WHERE (truck_number = ?) AND (temperature_in_celsius NOT BETWEEN 16 AND 20)
"""

def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    c.execute(sql_request, (truck_number, ))
    return len(c.fetchall()) >= 3

with sqlite3.connect('hw.db') as conn:
    print(check_if_vaccine_has_spoiled(conn.cursor(), 'а030ра178'))