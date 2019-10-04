import os
import unittest
from app import Routes

class BaseTest(unittest.TestCase):
    def setUp(self):
        Routes(self.APP).add_routes()

    def tearDown(self):
        pass
