from flask import jsonify

class Base(object):
    ROUTES = []

    def setter(self, **kwargs):
        for method in self._methods():
            if method in kwargs.keys():
                self.ROUTES += [
                    { 'url': kwargs[method]['url'], 'function': method, 'name': kwargs[method]['name'], 'kwargs': {'methods':[method.upper()]} },
                ]

    def get(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def post(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def patch(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def put(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def delete(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def on_success(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def on_error(self, **kwargs):
        return self.on(kwargs['response'], 500)

    def on_unauthorized(self, **kwargs):
        return self.on(kwargs['response'], 401)

    def on_not_found(self, **kwargs):
        return self.on(kwargs['response'], 404)

    def on(self, response, code):
        return response, code

    def json_response(self, dictionary):
        return jsonify(dictionary)

    def _methods(self):
        return ['get', 'post', 'put', 'delete', 'patch']
