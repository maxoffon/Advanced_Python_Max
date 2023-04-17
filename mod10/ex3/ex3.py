import sqlite3

if __name__ == "__main__":
    with sqlite3.connect('hw_3_database.db') as conn:
        cursor = conn.cursor()
        for table in ['table_1', 'table_2', 'table_3']:
            cursor.execute(f'SELECT COUNT(*) FROM {table}')
            print(f'В таблице {table} {cursor.fetchone()[0]} элементов')
        print()

        cursor.execute('SELECT DISTINCT COUNT(*) FROM table_1')
        print(f'Уникальных строк в таблице table_1: {cursor.fetchone()[0]}')
        print()

        cursor.execute('SELECT * '
                       'FROM table_1 '
                       'INTERSECT '
                       'SELECT *'
                       'FROM table_2')
        res3 = cursor.fetchone()
        res3 = 0 if res3 is None else res3[0]
        print(f'Количество общих элементов таблиц 1 и 2: {res3}')
        print()

        cursor.execute('SELECT * FROM table_1 '
                       'INTERSECT '
                       'SELECT * FROM table_2 '
                       'INTERSECT '
                       'SELECT * FROM table_3'
                       )
        res4 = cursor.fetchone()
        res4 = 0 if res4 is None else res4[0]
        print(f'Количество общих элементов таблиц 1, 2 и 3: {res4}')
        print()




