from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class GraphForm(FlaskForm):
    lower_bound = FloatField('Lower Bound', validators=[DataRequired()])
    upper_bound = FloatField('Upper Bound', validators=[DataRequired()])
    submit = SubmitField('Show Graph')