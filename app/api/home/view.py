from app.api import BaseApi

class Home(BaseApi):
    ROUTES = [
        { 'url': '/home', 'function': 'index', 'name': 'home', 'skip_auth': True },
        { 'url': '/home/create', 'function': 'create', 'name': 'home/create' },
        { 'url': '/home/hello', 'function': 'hello', 'name': 'home/hello' },
        { 'url': '/home/hi', 'function': 'hi', 'name': 'home/hi', 'kwargs': {'methods':['GET']} },
        { 'url': '/home/test/<name>', 'function': 'test', 'name': 'home/test', 'kwargs': {'methods':['GET', 'POST']} },
    ]

    def index(self):
        return super().index(response={'message': 'index'})

    def show(self):
        return super().show(response={'message': "show"})

    def create(self):
        return super().create(response={'message': "create"})

    def hello(self):
        return self.on_success(response={'message': 'hello'})

    def hi(self):
        return self.on_error(response={'message': 'hi'})

    def test(self, name):
        return self.on_success(response={"message": name})
