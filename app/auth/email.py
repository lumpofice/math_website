from flask import render_template, current_app
from app.email import send_email


def send_password_reset_email(user):
    '''This function generates a token that will be sent to the user via email,
once the ResetPasswordRequestForm has been validated.'''
    
    
    token = user.get_reset_password_token()
    
    
    send_email('[Math Website] Reset Your Password',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt',
            user=user, token=token),
        html_body=render_template('email/reset_password.html',
            user=user, token=token)
        )
