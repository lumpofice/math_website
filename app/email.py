from flask_mail import Message
from flask import render_template
from app import mail, app


def send_email(subject, sender, recipients, text_body,
    html_body):
    '''This method serves as the template for the email we send the user. The
msg variable calls the Message class from the flask_mail module and populates
it with the subject, sender, and recipients. From there, we assign the body and
html attributes to the .txt and .html files that make up the body of our
message.'''
    
    
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


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