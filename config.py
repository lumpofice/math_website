import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''The SECRET_KEY variable below is used to protect our web forms from
CSRF. The "SECRET_KEY" variable serving as argument within the get() function
is set by the application maintainer in the environment, while the string value
on the other side of the "or" statement is use in the absence of the
"SECRET_KEY": <"SECRET_KEY" value> key:value ordered pair within the dictionary
resulting from a call to os.environment.'''
    
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Eyop7n*n._;>"&6L'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['jparker@sasphs.net']
