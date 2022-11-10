import unittest
from django.test import Client


class RoadDog(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def recommend(self):
        response = self.client.post('/recommend/')
