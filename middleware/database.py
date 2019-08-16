class Database:
    def __init__(self, app=None):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)
