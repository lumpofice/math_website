'''importing the configuration file for the application'''
from config import Config

'''importing Pythong libraries and packages'''
import logging
from logging.handlers import SMTPHandler

'''importing flask methods, extensions, and libraries'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

'''flask-login extension, which keeps track of the user's logged-in state.'''
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


'''After the application instance is created:
importing objects, methods, and scripts from the application'''
from app import routes, models, errors


if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],\
            toaddrs=app.config['ADMINS'],\
            subject='Massive Discipline Failure',\
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)