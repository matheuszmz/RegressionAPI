from flask_wtf import FlaskForm
from wtforms import DecimalField, RadioField, SubmitField
from wtforms.validators import NumberRange


class NCForm(FlaskForm):
    c8_0 = DecimalField('C8:0', validators=[NumberRange()], default=0.0)
    c10_0 = DecimalField('C10:0', validators=[NumberRange()])
    c12_0 = DecimalField('C12:0', validators=[NumberRange()])
    c14_0 = DecimalField('C14:0', validators=[NumberRange()])
    c16_0 = DecimalField('C16:0', validators=[NumberRange()])
    c18_0 = DecimalField('C18:0', validators=[NumberRange()])
    c18_1 = DecimalField('C18:1', validators=[NumberRange()])
    c18_2 = DecimalField('C18:2', validators=[NumberRange()])
    c18_3 = DecimalField('C18:3', validators=[NumberRange()])
    c18_1_oh = DecimalField('C18:1 OH', validators=[NumberRange()])
    c20_0 = DecimalField('C20:0', validators=[NumberRange()])
    c20_1 = DecimalField('C20:1', validators=[NumberRange()])
    c22_1 = DecimalField('C22:1', validators=[NumberRange()])
    outros = DecimalField('Outros', validators=[NumberRange()])
    regression = RadioField(choices=[('pls', 'PLS Regression'), ('mlr', 'MLR Regression'), ('svr', 'SVR Regression')], default='pls')
    submit = SubmitField('Enviar')
