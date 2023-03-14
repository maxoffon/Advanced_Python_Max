from flask import Flask


app = Flask(__name__)


if __name__ == '__main__':
    app.run(__name__)


@app.route('/max_number/<path:nums>')
def hello_world(nums):
    try:
        numbers = [int(i) for i in nums.split('/')]
        return f'Максимальное число: <i>{max(numbers)}</i>'
    except ValueError:
        return 'Некорректный ввод'
