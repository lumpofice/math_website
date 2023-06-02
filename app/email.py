from flask_mail import Message
from app import mail
from threading import Thread
from flask import current_app


def send_async_email(app, msg):
    '''Flask pushes an application context automatically, but by starting a
custom thread---in the send_email function---we may be facing a situation in
which the application requires that we push a manual context.'''
    
    
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    '''This method serves as the template for the email we send the user. The
msg variable calls the Message class from the flask_mail module and populates
it with the subject, sender, and recipients. From there, we assign the body and
html attributes to the .txt and .html files, respectively, that make up the body
of our message.'''
    
    
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()
