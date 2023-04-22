'''importing flask methods and libraries'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from flask_babel import lazy_gettext as _1

'''importing objects, methods, and scripts from the application'''
from app.models import User


class LoginForm(FlaskForm):
    '''The login form encountered upon opening the website.'''
    
    
    username = StringField(_1('Username'), validators=[DataRequired()])
    password = PasswordField(_1('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_1('Remember Me'))
    submit = SubmitField(_1('Sign In'))
    
    
class RegistrationForm(FlaskForm):
    '''The registration form users will need to create their login
credentials'''
    
    
    username = StringField(_1('Username'), validators=[DataRequired()])
    email = StringField(_1('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_1('Password'), validators=[DataRequired()])
    password_again = PasswordField(_1('Repeat Password'),\
        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_1('Register'))
    
    
    def validate_username(self, username):
        '''This function ensures the username does not already exist
    within the data base.'''
        
        
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_1('Please use a different username.'))
        
        
    def validate_email(self, email):
        '''This function ensures the email does not already exist
    within the data base.'''
        
        
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_1('Please use a different email address.'))
        
        
class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_1('Email', validators=[DataRequired(), Email()]))
    submit = SubmitField(_1('Request Password Reset'))
    
    
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
        )
    submit = SubmitField('Request Password Reset')