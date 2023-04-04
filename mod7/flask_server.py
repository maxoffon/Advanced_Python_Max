import json

from flask import Flask, request

app = Flask(__name__)
logs = []


@app.route('/runcode_post', methods=["POST"])
def runcode_post():
    data = json.loads(request.get_data(as_text=True))
    logs.append(' | '.join([data['msg'], data['levelname']]))
    return 'ok'


@app.route('/runcode_get', methods=["GET"])
def runcode_get():
    return '<br>'.join(logs)


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
