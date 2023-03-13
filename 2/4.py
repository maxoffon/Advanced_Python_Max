from flask import Flask
from datetime import datetime


app = Flask(__name__)


if __name__ == '__main__':
    app.run(__name__)


weekdays = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    good_form = 'Хорошего' if weekday in [0, 1, 3, 6] else 'Хорошей'
    return f'Привет, {name}. {good_form} {weekdays[weekday]}!'


