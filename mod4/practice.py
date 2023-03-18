import json
from urllib.parse import unquote_plus

from flask import Flask, request
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import InputRequired
from wtforms.validators import NumberRange
from wtforms.validators import Email
from flask_wtf.form import FlaskForm

app = Flask(__name__)


@app.route('/sum1', methods=["POST"])
def sum1():
    array1 = request.form.getlist('array1', type=int)
    array2 = request.form.getlist('array2', type=int)

    result = ','.join(str(a1 + a2) for a1, a2 in zip(array1, array2))

    return f'Array of sums is [{result}]'

@app.route('/sum2', methods=["POST"])
def sum2():
    form_data = request.get_data(as_text=True)
    data = unquote_plus(form_data)
    print(data)

    arrays = {}

    for arr in data.split('&'):
        k, v = arr.split('=')
        arrays[k] = [int(i) for i in v.split(',')]

    result = ','.join([str(a1 + a2) for a1, a2 in zip(arrays['array1'], arrays['array2'])])

    return f'Array of sums is [{result}]'

@app.route('/sum3', methods=["POST"])
def sum3():
    form_data = request.get_data(as_text=True)

    json_data = json.loads(form_data)

    result = ','.join([str(a1 + a2) for a1, a2 in zip(json_data['array1'], json_data['array2'])])

    return f'Array of sums is [{result}]'


class RegistrationForm(FlaskForm):
    email = StringField(validators=[Email()])
    phone = IntegerField(validators=[InputRequired()])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField()
    comment = StringField()


class TicketForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    family_name = StringField(validators=[InputRequired()])
    ticket_num = IntegerField(validators=[InputRequired(), NumberRange(min=100000, max=999999)])


@app.route('/registration', methods=["POST"])
def reg():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f'Successfully registered user {email} with phone +7{phone}'
    return f'Incorrect input, {form.errors}', 400


@app.route('/ticket', methods=["POST"])
def ticket():
    form = TicketForm()

    if form.validate_on_submit():
        num = form.ticket_num.data
        if sum([int(i) for i in list(str(num // 10**3))]) == sum([int(i) for i in list(str(num % 10**3))]):
            return 'Поздравляем, у вас счастливый билет!'
        return 'К сожалению, у вас несчастливый билет, попробуйте ещё раз'
    return f'Incorrect input: {form.errors}'


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
