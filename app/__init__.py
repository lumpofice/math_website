'''importing the configuration file for the application'''
from config import Config

'''importing Pythong libraries and packages'''
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

'''importing flask methods, extensions, and libraries'''
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _1

'''flask-login extension, which keeps track of the user's logged-in state.'''
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message = _1('Log in to access this page.')
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)


'''From the errors folder in the app directory, we import bp, which is located
in the __init__.py file of error directory'''
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)


'''From the auth folder in the app directory, we import bp, which is located
in the __init__.py file of auth directory'''
from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')


'''From the main folder in the app directory, we import bp, which is located
in the __init__.py file of main directory'''
from app.main import bp as main_bp
app.register_blueprint(main_bp)


'''After the application instance is created:
importing objects, methods, and scripts from the application'''
from app import models, routes


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
            subject='Math Website Failure',\
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
        
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/math_website.log',\
        maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('Math Website startup')
    
    
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'es'


babel.init_app(app, locale_selector=get_locale)
