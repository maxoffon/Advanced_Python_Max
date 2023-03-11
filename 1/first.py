from datetime import timedelta, datetime
from flask import Flask
from random import choice
import re
import os

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route('/hello_world')
def hello_world():
    return 'Hello, world!'


marks = ['Chevrolet', 'Renault', 'Ford', 'Lada']
@app.route('/cars')
def cars():
    global marks
    return ', '.join(marks)


breeds = ['Корниш-рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'Манчкин']
@app.route('/cats')
def cats():
    global breeds
    return choice(breeds)


@app.route('/get_time/now')
def time():
    cur_time = datetime.now()
    return f'Точное время: {cur_time}'


@app.route('/get_time/future')
def time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


def get_words():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base_dir, 'war_and_peace.txt')
    with open(source, 'r') as f:
        text = ' '.join(f.readlines())
        return text


wnp = get_words()
@app.route('/get_random_word')
def war_and_peace():
    global wnp
    return choice(re.findall(r'\w+', wnp))


@app.route('/counter')
def counter():
    counter.visits += 1
    return str(counter.visits)


counter.visits = 0
