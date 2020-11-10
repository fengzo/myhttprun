# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.6, create time is 20-11-9 下午5:00 GMT+8

import multiprocessing
import time
import unittest
from . import api_server

class ApiServerUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_server_process = multiprocessing.Process(
            target=api_server.app.run
        )
        cls.api_server_process.start()
        time.sleep(0.1)
    @classmethod
    def tearDownClass(cls):
        cls.api_server_process.terminate()
