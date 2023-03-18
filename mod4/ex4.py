from flask import Flask
import shlex
import subprocess

app = Flask(__name__)


@app.route('/uptime', methods=["GET"])
def uptime():
    command_str = f"uptime -s"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True).stdout.decode()
    return f'Current uptime is {result}'


if __name__ == '__main__':
    app.run(debug=True)