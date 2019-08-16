from flask import jsonify
from conf.config import METHOD_DEFAULTS

class Base(object):

    def show(self, **kwargs):
        if 'id' not in kwargs.keys():
            return self.on_error(response={'message': 'missing ID'})
        return self.on(kwargs['response'], 200)

    def index(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def create(self, **kwargs):
        return self.on(kwargs['response'], 200)

    def update(self, **kwargs):
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

    def _rests(self):
        return [
            { 'methods': ['GET'], 'function': 'index' },
            { 'methods': ['GET'], 'function': 'show' },
            { 'methods': ['POST'], 'function': 'create' },
            { 'methods': ['PUT', 'PATCH'], 'function': 'update' },
            { 'methods': ['DELETE'], 'function': 'delete' },
        ]
