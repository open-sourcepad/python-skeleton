from app.api import BaseApi

class Home(BaseApi):
    BaseApi.ROUTES += [
            { 'url': '/home/hello', 'function': 'hello', 'name': 'home/hello', 'kwargs': {'methods':['GET']} },
            { 'url': '/home/hi', 'function': 'hi', 'name': 'home/hi', 'kwargs': {'methods':['GET']} },
            { 'url': '/home/test/<name>', 'function': 'test', 'name': 'home/test', 'kwargs': {'methods':['GET', 'POST']} },
        ]


    def __init__(self):
        routes = { 'get': { 'url': '/home', 'name': 'home' } }
        self.setter(**routes)

    def get(self):
        return self.on_success(response={'message': 'get'})

    def hello(self):
        return self.on_success(response={'message': 'hello'})

    def hi(self):
        return self.on_error(response={'message': 'hi'})

    def test(self, name):
        return self.on_success(response={"message": name})
