#!/usr/bin/env python
from config import Config
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    '''We have placed a new key "DATABASE_URL" and value "sqlite://" pair into
our dict(os.envirion) dictionary'''
    
    
    def setUp(self):
        '''We create an app_context attribute to allow us to access our
    current_app proxy. The db.create_all() call creates all of our tables.'''
        
        
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        
    def tearDown(self):
        '''We pop the app_context to tear down our current_app proxy'''
        
        
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
        
    def test_password_hashing(self):
        '''Here, we set up a user in our User model and test the
    "check_password" method'''
        
        
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
        
        
    def test_avatar(self):
        '''Here, we set up a user in our User model and test the avatar
    method'''
        
        
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
            'd4c74594d841139328695756648b6bd6?d=identicon&s=128'))
        
        
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
