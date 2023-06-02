import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    '''The SECRET_KEY variable below is used to protect our web forms from
CSRF. The "SECRET_KEY" dictionary key serving as argument within the
os.environ.get() call is set by the application maintainer in the
environment, while the string value on the other side of the "or" statement is
used in the absence of the "SECRET_KEY": <"SECRET_KEY" value> key:value ordered
pair within the dictionary that results from a call to os.environment.

There is no "DATABASE_URL":<"DATABASE_URL" value> key:value ordered pair
within dict(os.environ). Thus, we have a configured database, "app.db", located
within the master directory of the application, stored in the "basedir"
variable. The "MAIL_USE_TLS"
variable, on wich we stipulate a value other than None, encrypts data that we
transmit from the app to the destination with which we wish the app to make a
connection.

Finally, Flask-SQLAlchemy comes with an event notification system that uses
more resources when not explicitly set to "False". Given that we do not need
this event notification system, we have set this variable to "False".'''
    
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tryguessing'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['jparker@sasphs.net']
    POSTS_PER_PAGE = 10
    LANGUAGES = {'en', 'es'}
