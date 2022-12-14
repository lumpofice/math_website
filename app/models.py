'''importing python libraries and modules'''
from datetime import datetime
from hashlib import md5

'''importing objects, methods, and scripts from the application'''
from app import db, login

'''importing flask methods and libraries'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    '''This function takes the string representation of the unique user
identifier, stored in a user session storage space alotted by Flask, converts
that representation to an integer representation, then passes that integer
to the database for querying. The "id" argument comes from the primary key
column in the User model. This "id" is created through the User model in this
script; stored in the database to be retrieved as the user object for a given
session in the variable "current_user", the value of which is the "id".'''
    
    
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    '''This class stores the id, username, email, and password hash fields,
as well as any posts corresponding to a registered user. The one-to-many
relationship is between this class (from which we refer to the one) and the
Post class (to which we refer to the many). The name of the class through which
we refer to the many is passed to relationship(), and the backref parameter
to the relationship method serves as a User model attribute, allowing us to
access the author of the post.'''
    
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        '''This function prints username objects that are generated by this
    class and stored in the application's database. The specific user is
    accessed via their "id", which is set in this User model class.'''
        
        
        return '<User {}>'.format(self.username)
    
    
    def set_password(self, password):
        '''This function generates the password hash, using the password input
    to the appropriate position in the registration form. That password is
    accessed via the user object representing the client of the request at the
    time of registration. The password itself is not stored; only the password
    hash. '''
        
        
        self.password_hash = generate_password_hash(password)
        
        
    def check_password(self, password):
        '''This function passes the generated password hash, which was stored
    for the user at the time of registration,
    checking it with the password input by the user within the appropriate
    position of the login form. Meaning, the password input by the user at the
    time of login is compared with the password hash generated by this User
    model at the time of registration.'''
        
        
        return check_password_hash(self.password_hash, password)
    
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
    
    
class Post(db.Model):
    '''This class stores id, body, timestamp, and foreign key user_id
fields, the latter of which references the "id" field in the User model.'''
    
    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    def __repr__(self):
        '''This function prints post objects that are generated by this
    class and stored in the application's database. The specific post is
    accessed via the User class "id" field.'''
        
        
        return '<Post {}>'.format(self.body)