from flask import Flask
from datetime import datetime


app = Flask(__name__)


if __name__ == '__main__':
    app.run(__name__)


storage = {}
@app.route('/add/<date>/<int:number>')
def add(date, number):
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    storage.setdefault(year, [{}, 0])[0].setdefault(month, 0)
    storage[year][0][month] += number
    storage[year][1] += number
    return f'{day}.{month}.{year} было потрачено {number}'

@app.route('/calculate/<int:year>')
def calc_year(year):
    if year > datetime.now().year:
        return 'Невозможный год'
    y = str(year)
    year_exp = '0' if y not in storage else str(storage[y][1])
    return f'За {year} год было потрачено {year_exp}'


@app.route('/calculate/<int:year>/<int:month>')
def calc_year_month(year, month):
    if year > datetime.now().year or month > 12:
        return 'Неправильная дата'
    y = str(year)
    m = str(month)
    year_exp = '0' if y not in storage else str(storage[y][1])
    month_exp = '0' if y not in storage or m not in storage[y][0] else str(storage[y][0][m])
    return f'За {year} год было потрачено {year_exp}, ' \
           f'а за {month}-й месяц этого года - {month_exp}'
