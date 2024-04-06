# test_server.py
from flask_testing import TestCase
from server import app  # import your Flask application
import unittest

class TestServer(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_hello_endpoint(self):
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_smoker_endpoint(self):
        response = self.client.get('/api/instagram-analysis')
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()