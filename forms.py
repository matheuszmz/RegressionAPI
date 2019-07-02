from flask_wtf import FlaskForm
from wtforms import DecimalField, RadioField, SubmitField
from wtforms.validators import NumberRange


class NCForm(FlaskForm):
    c8_0 = DecimalField('C8:0', validators=[NumberRange()], default=0.00)
    c10_0 = DecimalField('C10:0', validators=[NumberRange()], default=0.00)
    c12_0 = DecimalField('C12:0', validators=[NumberRange()], default=0.00)
    c14_0 = DecimalField('C14:0', validators=[NumberRange()], default=0.00)
    c16_0 = DecimalField('C16:0', validators=[NumberRange()], default=0.00)
    c18_0 = DecimalField('C18:0', validators=[NumberRange()], default=0.00)
    c18_1 = DecimalField('C18:1', validators=[NumberRange()], default=0.00)
    c18_2 = DecimalField('C18:2', validators=[NumberRange()], default=0.00)
    c18_3 = DecimalField('C18:3', validators=[NumberRange()], default=0.00)
    c18_1_oh = DecimalField('C18:1 OH', validators=[NumberRange()], default=0.00)
    c20_0 = DecimalField('C20:0', validators=[NumberRange()], default=0.00)
    c20_1 = DecimalField('C20:1', validators=[NumberRange()], default=0.00)
    c22_1 = DecimalField('C22:1', validators=[NumberRange()], default=0.00)
    outros = DecimalField('Outros', validators=[NumberRange()], default=0.00)
    regression = RadioField(choices=[('pls', 'PLS Regression'), ('mlr', 'MLR Regression'), ('svr', 'SVR Regression')], default='pls')
    submit = SubmitField('Enviar')
