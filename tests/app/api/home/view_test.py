import unittest
from unittest import mock
from flask import Flask
import flask_restful
from tests.base_test import BaseTest

class ViewTest(BaseTest):
    APP = Flask('__main__')

    def setUp(self):
        super().setUp()

    def test_home(self):
        with self.APP.test_client() as client:
            resp = client.get('/home')
            self.assertEquals(resp.status_code, 200)
            self.assertEquals(resp.get_json(), {'message': 'index'})
