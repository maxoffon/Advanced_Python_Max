import sqlite3

if __name__ == "__main__":
    with sqlite3.connect('hw_2_database.db') as conn:
        with open('report.md', 'w', encoding='utf-8') as report:
            report.write('# Ответы на вопросы задачи 2: #\n')
            cursor = conn.cursor()

            cursor.execute("SELECT phone_color, MAX(sold_count) FROM table_checkout")
            res1 = cursor.fetchone()
            report.write(f'1. Самый покупаемый цвет: *{res1[0]}*; Его купили в количестве раз: *{res1[1]}*<br>\n***\n')

            cursor.execute("SELECT * "
                           "FROM table_checkout "
                           "WHERE phone_color in ('Red', 'Blue')")
            res2 = cursor.fetchall()
            diff = res2[0][1] - res2[1][1]
            report.write(f'2. Телефоны цвета *{res2[0][0]}* купили больше на *{diff}* штук, чем цвета *{res2[1][0]}*<br>\n***\n') \
                if diff >= 0 \
                else report.write(f'2. Телефоны цвета *{res2[1][0]}* купили больше на *{-diff}* штук, чем цвета *{res2[0][0]}*<br>\n***\n')

            cursor.execute("SELECT phone_color, MIN(sold_count) FROM table_checkout")
            res3 = cursor.fetchone()
            report.write(f'3. Самый непопулярный цвет: *{res3[0]}*; Его купили в количестве раз: *{res3[1]}*<br>\n')