import unittest
from flask import Flask
from flask_testing import TestCase
from main import app

class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Web App', response.data)

    def test_about(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My name is Ahmed , Iam a DevOps Engineer.', response.data)

    def test_contact(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You can reach me via email at', response.data)

if __name__ == '__main__':
    unittest.main()
