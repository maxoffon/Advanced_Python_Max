import sqlite3

with sqlite3.connect('hw_4_database.db') as conn:
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM salaries WHERE salary < 5000')
    res1 = cursor.fetchone()
    res1 = 0 if res1 is None else res1[0]
    print(f'За чертой бедности живут люди в количестве: {res1}')
    print()

    cursor.execute('SELECT AVG(salary) FROM salaries')
    print(f'Средняя зарплата по острову: {cursor.fetchone()[0]}')
    print()

    cursor.execute('SELECT * FROM salaries ORDER BY salary')
    res2 = cursor.fetchall()
    print(f'Медианная зарплата по острову: {res2[len(res2) // 2][1]}')
    print()

    cursor.execute('SELECT 100 * ROUND('
                   '(SELECT SUM(salary) FROM salaries ORDER BY salary DESC '
                   'LIMIT 0.1 * (SELECT COUNT(*) FROM salaries)) /'
                   '(SELECT SUM(salary) FROM salaries ORDER BY salary '
                   'LIMIT 0.9 * (SELECT COUNT(*) FROM salaries)), 2)')
    res3 = cursor.fetchall()
    print(f'Процент социального неравенства F: {res3[0][0]}')
    print()

