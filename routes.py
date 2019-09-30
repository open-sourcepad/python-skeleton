from flask import request, session
import re

from app import db
from app.api import *
from app.models import User

class Routes:
    VIEWS = [
        PostsApi,
        UsersApi,
    ]

    METHOD_DEFAULTS = {
        'index': ['GET'],
        'show': ['GET'],
        'create': ['POST'],
        'update': ['PUT', 'PATCH'],
        'delete': ['DELETE'] }

    @classmethod
    def init_app(cls, app):
        for view in cls.VIEWS:
            view_instance = view()
            for route in view_instance._routes():
                func = getattr(view_instance, route['function'], None)
                if func:
                    methods = route.get('methods') or cls.METHOD_DEFAULTS.get(route['function'], ['GET'])

                    if 'skip_auth' not in route:
                        func = cls.auth_handler(func)
                    func = cls.db_error_handler(func)

                    app.add_url_rule(
                        route['url'],
                        f"{route['url']}#{route['function']}",
                        func,
                        methods=methods)

    @classmethod
    def auth_handler(cls, func):
        def new_func(**kwargs):
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if token:
                user = User.find_by_token(token)
                if user:
                    session['user'] = user.to_dict()
                    return func(**kwargs)
            return {'error': 'Unauthorized'}, 401
        return new_func

    @classmethod
    def db_error_handler(cls, func):
        def new_func(**kwargs):
            try:
                return func(**kwargs)
            except Exception as e:
                error = str(e)
                if re.search('(MySQL server has gone away|until invalid transaction is rolled back)', error):
                    db.session.rollback()
                    User.query.count() # any sql call
                    return func(**kwargs)
                if error == 'Signature has expired':
                    return {'error': 'Expired session'}, 401
                raise e
            return func()
        return new_func
