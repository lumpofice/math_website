'''importing flask methods, extensions, and libraries'''
from flask import Flask
from config import Config
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


'''importing objects, methods, and scripts from the application'''
from app import routes, models
