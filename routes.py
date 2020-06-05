from flask import request, session
import re

from app import db
from app.api import *

class Routes:
    VIEWS = [
    ]

    METHOD_DEFAULTS = {
        'index': ['GET'],
        'show': ['GET'],
        'create': ['POST'],
        'update': ['PUT', 'PATCH'],
        'delete': ['DELETE'] }

    @classmethod
    def _list_routes(self):
        import sys
        filter = None if len(sys.argv) < 2 else sys.argv[1]
        just = 15
        print(f" {'Function'.ljust(just)} \t {'URL'.ljust(just)} \t Methods \t Skip Auth")
        print("--------------------------------------------------------------------------------------------------")
        for view in self.VIEWS:
            results = getattr(view, 'ROUTES', [])
            for result in results:
                if filter is None or filter in str(result) or filter in view.__name__.lower():
                    print(f" {view.__name__}#{result['function'].ljust(10)} \t {result['url'].ljust(just)} \t {result['methods']} \t {result['skip_auth']}")



    def init_app(self, app):
        for view in self.VIEWS:
            view_instance = view()
            for route in view_instance._routes():
                func = getattr(view_instance, route['function'], None)
                if func:
                    methods = route.get('methods') or self.METHOD_DEFAULTS.get(route['function'], ['GET'])

                    if 'skip_auth' not in route:
                        func = self.auth_handler(func)
                    func = self.db_error_handler(func)

                    app.add_url_rule(
                        route['url'],
                        f"{route['url']}#{route['function']}",
                        func,
                        methods=methods)

    def auth_handler(self, func):
        def new_func(**kwargs):
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if token:
                user = User.find_by_token(token)
                if user:
                    session['user'] = user.to_dict()
                    return func(**kwargs)
            return {'error': 'Unauthorized'}, 401
        return new_func

    def db_error_handler(self, func):
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

if __name__ == '__main__':
    Routes._list_routes()
