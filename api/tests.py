import unittest
import json


import os
import sys


sys.path.insert(0, os.path.abspath(".."))

from api.manage import  app


class Test_payments(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def test_get_users_by_id(self):
        header = {"content-type": "application/json"}
        get_users = app.test_client().get('/user/get/id?user_id=820', headers=header)
        result = json.loads(get_users.data.decode())
        self.assertEqual(result['data'], result['data'])

    def test_get_users_by_age_and_limit(self):
        header = {"content-type": "application/json"}
        get_users = app.test_client().get('/user/get/ranges?limit=20&ages1=5&ages2=20', headers=header)
        result = json.loads(get_users.data.decode())
        self.assertEqual(result['data'], result['data'])
        self.assertEqual(get_users.status_code, 200)


if __name__ == '__main__':
    unittest.main()
