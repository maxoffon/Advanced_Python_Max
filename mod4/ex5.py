import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/ps', methods=["GET"])
def ps():
    args = request.args.getlist('arg')
    args_clean = [shlex.quote(s) for s in args]
    command_str = f"ps {' '.join(args_clean)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Error", 500

    return f'<pre>{result.stdout.decode()}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
