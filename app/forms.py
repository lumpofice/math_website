'''importing flask methods and libraries'''
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, IntegerField,\
     PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired,\
     ValidationError, Email, EqualTo, Length

'''importing objects, methods, and scripts from the application'''
from app.models import User
    
    
class LoginForm(FlaskForm):
    '''The login form encountered upon opening the website.'''
    
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class RegistrationForm(FlaskForm):
    '''The registration form users will need to create their login
credentials'''
    
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat Password',\
        validators=[DataRequired(),\
        EqualTo('password')])
    submit = SubmitField('Register')
    
    
    def validate_username(self, username):
        '''This function ensures the username does not already exist
    within the data base.'''
        
        
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
        
        
    def validate_email(self, email):
        '''This function ensures the email does not already exist
    within the data base.'''
        
        
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    
class GeometricSeriesForm(FlaskForm):
    '''The form users encounter when they venture to see a graph of the
geometric series.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed polynomial degree 1 functions.'''
    
    
    horizontal_shift = FloatField('Choose a horizontal shift between -5 and 5',\
        validators=[InputRequired(), NumberRange(-5, 5)])
    y_scalar = FloatField('Choose a y_scalar between -5 and 5',\
        validators=[InputRequired(), NumberRange(-5, 5)])
    vertical_shift = FloatField('Choose a vertical shift between -5 and 5',\
        validators=[InputRequired(), NumberRange(-5, 5)])
    submit = SubmitField('Show Graph')
    
    
class PolynomialDegree2TransformForm(FlaskForm):
    '''The form users encounter when they venture to see a graph of the
parent and transformed polynomial degree 2 functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed polynomial degree 3 functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed reciprocal functions, which is a rational function
where the numerator is a polynomial of degree 0 and the denominator is a
polynomial of degree 1.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed square root functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed cube root functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed absolute value functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed general exponential functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed general logarithmic functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed base e exponential functions.'''
    
    
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
    '''The form users encounter when they venture to see a graph of the
parent and transformed base e logarithmic functions.'''
    
    
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