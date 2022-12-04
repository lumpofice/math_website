from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, IntegerField,\
     PasswordField, BooleanField
from wtforms.validators import DataRequired, NumberRange, InputRequired,\
     ValidationError, Email, EqualTo
from app.models import User
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat Password',\
        validators=[DataRequired(),\
        EqualTo('password')])
    submit = SubmitField('Register')
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
        
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    
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
    

class PolynomialDegree1TransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class PolynomialDegree2TransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class PolynomialDegree3TransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class ReciprocalDegree0ByDegree1TransformForm(FlaskForm):
    horizontal_shift = IntegerField(\
    'Choose an integer horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = IntegerField(\
    'Choose an integer x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = IntegerField('Choose an integer y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = IntegerField(\
    'Choose an integer vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    

class SquareRootTransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class CubeRootTransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')


class AbsoluteValueTransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    

class GeneralExponentialTransformForm(FlaskForm):
    base = FloatField('Choose a base between 0.1 and 3.1',\
    validators=[InputRequired(), NumberRange(0.1, 3.1)])
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    

class GeneralLogarithmicTransformForm(FlaskForm):
    base = FloatField('Choose a base between 0.1 and 3.1',\
    validators=[InputRequired(), NumberRange(0.1, 3.1)])
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class BaseEExponentialTransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class BaseELogarithmicTransformForm(FlaskForm):
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    x_scalar = FloatField(\
    'Choose a x_scalar between 0 and 5',\
    validators=[InputRequired(), NumberRange(0, 5)])
    x_reflection = IntegerField(\
    'If an x_reflection is desired, choose -1, else choose 1',\
    validators=[InputRequired(), NumberRange(-1, 1)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
    validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')