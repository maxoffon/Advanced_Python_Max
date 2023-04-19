"""
На заводе "Дружба" работает очень дружный коллектив.
Рабочие работают посменно, в смене -- 10 человек.
На смену заходит 366 .

Бухгалтер завода составила расписание смен и занесла его в базу данных
    в таблицу `table_work_schedule`, но совершенно не учла тот факт,
    что все сотрудники люди спортивные и ходят на различные спортивные кружки:
        1. футбол (проходит по понедельникам)
        2. хоккей (по вторникам
        3. шахматы (среды)
        4. SUP сёрфинг (четверг)
        5. бокс (пятница)
        6. Dota2 (суббота)
        7. шах-бокс (воскресенье)

Как вы видите, тренировки по этим видам спорта проходят в определённый день недели.

Пожалуйста помогите изменить расписание смен с учётом личных предпочтений коллектива
    (или докажите, что то, чего они хотят - невозможно).
"""
import sqlite3, datetime

req_update = """
UPDATE table_friendship_schedule
SET employee_id = ?
WHERE employee_id = ? AND date = ?
"""

SPORTS = {'футбол': 'понедельник',
          'хоккей': 'вторник',
          'шахматы': 'среда',
          'SUP сёрфинг': 'четверг',
          'бокс': 'пятница',
          'Dota2': 'суббота',
          'шах-бокс': 'воскресенье'}

weekdays = {0: 'понедельник',
          1: 'вторник',
          2: 'среда',
          3: 'четверг',
          4: 'пятница',
          5: 'суббота',
          6: 'воскресенье'}

def get_weekday(string: str) -> str:
    date = datetime.datetime.weekday(get_date(string))
    return weekdays[date]

def get_date(string: str) -> datetime.date:
    year, month, day = map(int, string.split('-'))
    return datetime.datetime(year, month, day)

def get_shift_number(date: datetime.date) -> int:
    return (date - get_date('2020-01-01')).days + 1


def update_work_schedule(c: sqlite3.Cursor) -> None:
    changes = []
    c.execute("SELECT t1.employee_id, t1.date, t2.name, t2.preferable_sport "
              "FROM table_friendship_schedule AS t1 "
              "INNER JOIN table_friendship_employees as t2 "
              "ON t1.employee_id = t2.id")
    res = [item for item in c.fetchall() if get_weekday(item[1]) == SPORTS[item[3]]]
    changed_indexes = []
    possible_to_change = True
    for i in range(len(res)):
        if i in changed_indexes:
            continue
        j = len(res) - 1
        shift_from = get_shift_number(get_date(res[i][1]))
        shift_to = get_shift_number(get_date(res[j][1])) # Чтобы работник не повторялся в одной смене дважды
        while not (not (shift_from <= res[j][0] <= shift_from + 9)
                   and not (shift_to <= res[i][0] <= shift_to + 9) # Чтобы работник не повторялся в одной смене дважды
                   and res[j][3] != res[i][3]
                   and j not in changed_indexes):
            j -= 1
            if j == i:
                possible_to_change = False
                print('Нельзя разрешить конфликты всех работников. '
                      'Меняю план в соответствии с найденными возможными перестановками')
                break
        if not possible_to_change:
            for item in changes:
                from_, date_from, to_, date_to = item
                c.execute(req_update, (to_, from_, date_from))
                c.execute(req_update, (from_, to_, date_to))
            break
        else:
            changes.append((res[i][0], res[i][1], res[j][0], res[j][1]))
            changed_indexes.append(j)

    if possible_to_change:
        for item in changes:
            from_, date_from, to_, date_to = item
            c.execute(req_update, (to_, from_, date_from))
            c.execute(req_update, (from_, to_, date_to))



with sqlite3.connect('hw.db') as conn:
    c = conn.cursor()
    update_work_schedule(c)
