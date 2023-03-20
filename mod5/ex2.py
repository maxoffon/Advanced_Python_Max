from flask import Flask
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.form import FlaskForm
from subprocess import Popen, TimeoutExpired, PIPE
import shlex


app = Flask(__name__)


class ValidationForm(FlaskForm):
    code = StringField(validators=[InputRequired(message='Обязательно введите исполняемый код')])
    timeout = IntegerField(default=10)


@app.route('/runcode', methods=["POST"])
def runcode():
    form = ValidationForm()
    if form.validate_on_submit():
        cmd = shlex.split(f'py -c "{form.code.data}"')
        timeout = form.timeout.data
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        if proc.stderr.readline():
            return f'Некорректный ввод', 400
        try:
            outs, errs = proc.communicate(timeout=timeout)
            killed = False
        except TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            killed = True
        return f'Результат работы: stdout: {outs.decode()}, stderr: {errs.decode()}, killed by timeout: {killed}'
    return f'Ошибка в запросе: {form.errors}', 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
