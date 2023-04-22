from flask import render_template
from app.email import send_email
from app import app


def send_password_reset_email(user):
    '''This function generates a token that will be sent to the user via email,
once the ResetPasswordRequestForm has been validated. We use the send_email
method above to email the user with the desired contents of our message.'''
    
    
    token = user.get_reset_password_token()
    
    
    send_email('[Massive Discipline] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
            user=user, token=token),
        html_body=render_template('email/reset_password.html',
            user=user, token=token)
        )