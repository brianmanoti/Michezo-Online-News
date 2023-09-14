import unittest
from flask import Flask
from app import app, db
from app.models.user import User

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use a test database
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_success(self):
        # Create a test user
        user = User(username='testuser', password='password')
        db.session.add(user)
        db.session.commit()

        # Simulate a login request with valid credentials
        response = self.app.post('/login', data={'username': 'testuser', 'password': 'password'}, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in successfully.', response.data)

    def test_login_failure(self):
        # Simulate a login request with invalid credentials
        response = self.app.post('/login', data={'username': 'nonexistentuser', 'password': 'wrongpassword'}, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login failed. Please check your credentials.', response.data)

if __name__ == '__main__':
    unittest.main()
