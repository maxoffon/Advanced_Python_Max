from flask import Flask

app = Flask(__name__)


@app.route('/test')
def uptime():
    return 'test'


if __name__ == '__main__':
    app.run(debug=True)
