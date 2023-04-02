from flask import Flask

app = Flask(__name__)


@app.route('/runcode_post', methods=["POST"])
def runcode_post():
    return 'OK'


@app.route('/runcode_get', methods=["GET"])
def runcode_get():
    return 'OK'


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
