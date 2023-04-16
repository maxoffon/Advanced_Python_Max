import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

root = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(root, 'templates')
js_path = os.path.join(template_path, 'js')


@app.route("/")
def hello_world():
        return render_template('index.html')

@app.route("/js/<path:path>")
def send_js(path):
        return send_from_directory(js_path, path)


if __name__ == '__main__':
    app.run(debug=True)
