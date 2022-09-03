from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
    

class ChooseFunction(FlaskForm):
    submit = SubmitField('geometric')
    
    
class GeometricForm(FlaskForm):
    base = FloatField('Base', validators=[DataRequired()])
    scalar = FloatField('Scalar', validators=[DataRequired()])
    submit = SubmitField('Show Graph')