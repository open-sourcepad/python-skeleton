import pytest
from flask import json

from run import app

def test_usersapi_status_code():
    res = app.test_client().get('/test', json=dict(test=123))

    assert json.loads(res.data) == {'test': 123}
    assert res.status_code == 200
