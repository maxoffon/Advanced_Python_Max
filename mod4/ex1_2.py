from typing import Optional
from flask import Flask
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, ValidationError
from flask_wtf.form import FlaskForm

app = Flask(__name__)


def number_length(minimum: int, maximum: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        try:
            if not minimum <= form.data[field.name] <= maximum:
                raise ValidationError(message=message)
        except TypeError:
            raise ValidationError(message='Неверный тип данных')

    return _number_length


class NumberLength:
    def __init__(self, minimum, maximum, message=None):
        self.minimum = minimum
        self.maximum = maximum
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        try:
            if not self.minimum <= form.data[field.name] <= self.maximum:
                raise ValidationError(message=self.message)
        except TypeError:
            pass


class RegistrationForm(FlaskForm):
    email = StringField(validators=[Email(message='Неверный формат email'),
                                    InputRequired(message='Обязательное поле для заполнения')])
    phone = IntegerField(validators=[InputRequired(message='Обязательное поле для заполнения'),
                                     NumberLength(10 ** 9, 9999999999, 'Число вне допустимых границ')])
    phone2 = IntegerField(validators=[InputRequired(message='Обязательное поле для заполнения'),
                                      number_length(10 ** 9, 9999999999, 'Число вне допустимых границ')])
    name = StringField(validators=[InputRequired(message='Обязательное поле для заполнения')])
    address = StringField(validators=[InputRequired(message='Обязательное поле для заполнения')])
    index = IntegerField(validators=[InputRequired(message='Обязательное поле для заполнения')])
    comment = StringField()


@app.route('/registration', methods=["POST"])
def reg():
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        return f'User {name} successfully registered!'
    return f'Incorrect input: {form.errors}', 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
