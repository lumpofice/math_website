#!/usr/bin/env python
from config import Config
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post


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
        
        
    def test_follow(self):
        '''The first two assertEqual() calls will confirm that u1 is neither
    following ("followed") nor is being followed ("followers") by anyone.'''
        
        
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])
        
        
        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')
        
        
        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)
        
        
    def test_follow_posts(self):
        '''Here, we set up 4 users. For each user, we create a post. We add
    all users and posts to the database. We set up a user-to-user follow
    relationship, then we grab all of the posts from the users, followed by a
    specific user, and the user have posted. We assert that what our test
    database contains is precisely the user-to-user follow relationship we have
    constructed, testing the list of followed posts for each user.'''
        
        
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])
        
        
        now = datetime.utcnow()
        p1 = Post(body='post from john', author=u1,
            timestamp=now + timedelta(seconds=1))
        p2 = Post(body='post from susan', author=u2,
            timestamp=now + timedelta(seconds=4))
        p3 = Post(body='post from mary', author=u3,
            timestamp=now + timedelta(seconds=3))
        p4 = Post(body='post from david', author=u4,
            timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        
        
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()
        
        
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)