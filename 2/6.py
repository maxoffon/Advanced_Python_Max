from flask import Flask
import os


app = Flask(__name__)


if __name__ == '__main__':
    app.run(__name__)


@app.route('/preview/<int:size>/<path:rel_path>')
def hello_world(size, rel_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(base_dir, rel_path)
    with open(abs_path, 'r') as f:
        string = f.read(size)
        return f'<b>{abs_path}</b> {len(string)}<br>{string}'