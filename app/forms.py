from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired
    
    
class GeometricSeriesForm(FlaskForm):
    base = FloatField('Choose a base "r" between -0.99 and 0.99 inclusive',\
    validators=[InputRequired(),\
    NumberRange(-0.99, 0.99)])
    scalar = FloatField('Choose a real scalar "a" between -1000 and 1000'\
    ' inclusive', validators=[InputRequired(), NumberRange(-1000, 1000)])
    epsilon = FloatField('Choose an epsilon between 0.00001 and 1 inclusive',\
    validators=[InputRequired(),\
    NumberRange(0.00001, 1)])
    large_m = IntegerField('Choose a large integer "m" between 1 and 1000'\
    ' inclusive', validators=[InputRequired(), NumberRange(1, 1000)])
    submit = SubmitField('Show Graph')
    

class PolynomialDegree2TransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')

