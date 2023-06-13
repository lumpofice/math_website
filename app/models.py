'''importing python libraries and modules'''
from datetime import datetime
from hashlib import md5
from time import time
import jwt

'''importing objects, methods, and scripts from the application'''
from app import db, login
from flask import current_app

'''importing flask methods and libraries'''
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class User(UserMixin, db.Model):
    '''This class stores the id, username, email, and password hash fields,
as well as any posts corresponding to a registered user. The one-to-many
relationship is between this class (from which we refer to the one) and the
Post class (to which we refer to the many). The name of the class through which
we refer to the many is passed to relationship(), and the backref parameter
to the relationship method serves as a User model attribute, allowing us to
access the author of the post.

The follower_id column of the
association table (followers) stores the "id" of the user from the User model,
same as the User model "id" stored in the followed_id column of this
association table.

As this is a
many-to-many relationship we are setting up, the association (or helper) table
will be the value for the "secondary" parameter in the argument of the
db.relationship call of the followed table. This association table is
populated with the relationships between user id field values as users follow
and are being followed.

In the followed table, the "c" in ".c." is an attribute of SQLAlchemy tables
not defined as models. There are sub-attributes of this "c" attribute, and it
is to these sub-attributes that the table columns are exposed.
The "dynamic" value for the lazy parameter in the db.backref call executes
the right-hand side of this connection (followers), while the "dynamic" value
for the lazy parameter of the db.relationship call executes the left-hand side
of this connection (followed). Both of these "dynamic" values on their
respective lazy parameters ensures the respective queries are not run until
requested.
'''
    
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    
    
    def __repr__(self):
        '''This function prints username objects that are generated by this
    class and stored in the application's database. The specific user is
    accessed via their "id", which is set in this User model class.'''
        
        
        return '<User {}>'.format(self.username)
    
    
    def set_password(self, password):
        '''This function generates the password hash, using the password input
    to the appropriate position in the RegistrationForm.
    The password itself is not stored; only the password
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
    
    
    def get_reset_password_token(self, expires_in=600):
        '''This method uses the JSON Web Tokens module to generate a web token
    to be embedded within the password reset link provided within the
    password reset email sent at the request of the user.'''
        
        
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256'
            )
    
    
    @staticmethod
    def verify_reset_password_token(token):
        '''This method attempts to decode the JSON Web Token, before passing
    the result/value of that attempt to the User object,
    via the User.verify_reset_password_token function call within the
    reset_password method of the routes.py file, with which the reset_password
    method determines, via a Boolean value, whether to keep you in the
    reset_password view or to redirect you to the index view.'''
        
        
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
    
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
    
    
    
    
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
    
    
    
    
