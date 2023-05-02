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
pair within the dictionary resulting from a call to os.environment.

As of 01/20/23, there is no key:value pair set by the maintainer for
"SECRET_KEY".

import os
import pprint
env_var = os.environ
pprint.pprint(dict(env_var), width = 1)

Also, there is no "DATABASE_URL":<"DATABASE_URL" value> key:value ordered pair
within dict(os.environ). Thus, we have a configured database, "app.db", located
within the master directory of the application, stored in the "basedir"
variable. None of "MAIL_SERVER", "MAIL_PORT", "MAIL_USE_TLS", "MAIL_USERNAME",
nor "MAIL_PASSWORD" exist as keys in dict(os.environ). The "MAIL_USE_TLS"
variable, on wich we stipulate a value other than None, encrypts data that we
transmit from the app to the destination with which we wish the app to make a
connection.

As of 03/04/23, we have setup a mailtrap.io account that captures emails sent
from the terminal. We can set up environment variables per terminal session
and run code in that populated terminal to achieve this capture, with the
following:


export MAIL_SERVER=sandbox.smtp.mailtrap.io
export MAIL_PORT=2525
export MAIL_USERNAME=
export MAIL_PASSWORD=
export MAIL_USE_TLS=True
export MAIL_USE_SSL=False
. venv/bin/activate
flask shell
from flask_mail import Message
from app import mail
msg = Message('test subject', sender='jparker@sasphs.net',
    recipients=['jparker@sasphs.net'])
msg.body = 'does it work?'
mail.send(msg)


As of 03/08/23, we have full use of the password reset feature that uses email
to prompt users towards accomplishing a password reset successfully. We are
using the gmail server for this, with the following environment variables:


export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USERNAME=
export MAIL_PASSWORD=
export MAIL_USE_TLS=1


As of 01/21/23, we have error messages sent to a terminal on the local machine.

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
