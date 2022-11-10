import unittest
from django.test import Client

class Accounts(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def signup(self):
        response = self.client.post('/accounts/signup/', {'username': 'john2'
            , 'password1': '123qwe!@#QWE'
            , 'password2': '123qwe!@#QWE'
            , 'email': 'aaa@bbb.com'
            , 'tel': '010-0000-1111'
            , 'addr': 'seoul'
            , 'name':'md'
            , 'addr_detail': 'gangnam'})

        self.assertEqual(response.url, '/')
