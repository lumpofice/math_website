'''importing flask methods and libraries'''
from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, SubmitField, TextAreaField, FloatField,\
    SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length,\
    NumberRange, InputRequired
from flask_babel import lazy_gettext as _1

'''importing objects, methods, and scripts from the application'''
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_1('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_1('About me'),
        validators=[Length(min=0, max=140)])
    submit = SubmitField(_1('Submit'))
    
    
    '''Below is the code that obviates the 500 error handler template and
instead flashes an error message below the form line. Testing changes to the
structure of the app, say during Blueprint implementation, will require us to
comment out the below code so that the 500 error message template will
display.'''
    
    
    def __init__(self, original_username, *args, **kwargs):
        '''The original_username variable here corresponds to the
    current_user.username argument passed to the EditProfileForm in the
    outes.py file.'''
        
        
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        
        
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_1('Please use a different username.'))
            

class EmptyForm(FlaskForm):
    '''This is the button that will appear accordingly as "Follow" and
"Unfollow" as current_user browses the profile pages of other users'''
    
    
    submit = SubmitField('submit')
    
    
class PostForm(FlaskForm):
    '''With this form, we can post from our destination of choice, which will
be the index page.'''
    
    
    post = TextAreaField('Say it!', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
    
    
# FUNCTIONS---------------------------------------------------------------------
# FUNCTIONS---------------------------------------------------------------------
# FUNCTIONS---------------------------------------------------------------------
# FUNCTIONS--------------------------------------------------------------------- 
    
    
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
