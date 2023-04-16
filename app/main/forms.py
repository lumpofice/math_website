'''importing flask methods and libraries'''
from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, FloatField, SubmitField, IntegerField,\
     PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired,\
     ValidationError, Email, EqualTo, Length
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