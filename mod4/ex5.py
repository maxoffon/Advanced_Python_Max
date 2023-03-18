import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/ps', methods=["GET"])
def ps():
    args = request.args.getlist('arg')
    print(args)
    result = subprocess.run(args, capture_output=True).stdout.decode()
    return f'Result: <pre>{result}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
