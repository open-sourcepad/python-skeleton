import requests
from .base import Base, ExceptionBase

class CallbackError(ExceptionBase):
    pass

class Callback(Base):
    def __init__(self, method='post', url='', data={}, json={}, headers={}):
        self.req = getattr(requests, method)
        self.url = url
        self.data = data
        self.json = json
        self.headers = headers

    def request(self):
        try:
            result = self.req(self.url, data=self.data, json=self.json, headers=self.headers)
            return result
        except Exception as e:
            return CallbackError(
                f"Callback error.\nError: {e}",
                file='callback_error'
            )
