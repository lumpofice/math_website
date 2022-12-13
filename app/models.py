'''importing python libraries'''
from datetime import datetime

'''importing objects, methods, and scripts from the application'''
from app import db, login

'''importing flask methods and libraries'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    '''This function take the string representation of the user id, converts
that representation to an integer representation, then passes that integer
to the database for querying.'''
    
    
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    '''This class stores the id, username, email, and password hash fields,
as well as any posts corresponding to a registered user.'''
    
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    
    def __repr__(self):
        '''This function prints objects of this class.'''
        
        
        return '<User {}>'.format(self.username)
    
    
    def set_password(self, password):
        '''This function generates the password hash, using the password input
    to the appropriate position in the registration form.'''
        
        
        self.password_hash = generate_password_hash(password)
        
        
    def check_password(self, password):
        '''This function passes the generated password hash stored for the user,
    checking it with the password input by the user within the appropriate
    position of the login form.'''
        
        
        return check_password_hash(self.password_hash, password)
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)