# tests/test_auth_service.py

import unittest
from flask import json
from auth_service.app import app, db

class AuthServiceTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/test_db'  # Use the testing database
        self.app = app.test_client()
        with app.app_context():
            db.create_all()  # Create tables in the testing database

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()  # Drop tables after testing

    def test_signup(self):
        # Test user registration endpoint
        data = {'username': 'test_user', 'password': 'test_password'}
        response = self.app.post('/signup', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User signed up successfully', response.data)

    def test_login(self):
        # Test user login endpoint
        data = {'username': 'test_user', 'password': 'test_password'}
        self.app.post('/signup', data=json.dumps(data), content_type='application/json')
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User logged in successfully', response.data)

    # Add more tests for other endpoints and functionality

if __name__ == '__main__':
    unittest.main()
