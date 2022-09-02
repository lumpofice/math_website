from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class GraphForm(FlaskForm):
    base = FloatField('Base', validators=[DataRequired()])
    scalar = FloatField('Scalar', validators=[DataRequired()])
    submit = SubmitField('Show Graph')