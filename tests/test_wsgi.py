import random

from flask_testing import TestCase
from wsgi import app

random.randint(1,6)

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    def test_one_roll(self):
        roll = self.client.get('/').json['roll']
        self.assertIsInstance(roll, int)
        self.assertGreater(roll, -10)
        self.assertLess(roll, 7)