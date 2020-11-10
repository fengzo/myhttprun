# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6, create time is 20-11-9 下午5:41 GMT+8

import requests
from .base import ApiServerUnittest

class TestApiServer(ApiServerUnittest):
    def setUp(self):
        super(TestApiServer, self).setUp()
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()
        self.clear_users()
    def tearDown(self):
        super(TestApiServer, self).tearDown()
    def test_create_user_not_existed(self):
        self.clear_users()

        url = "%s/api/users/%d" % (self.host, 1000)
        data = {
            "name": "user1",
            "password": "123456"
        }
        resp = self.api_client.post(url, json=data)

        self.assertEqual(201, resp.status_code)
        self.assertEqual(True, resp.json()["success"])

