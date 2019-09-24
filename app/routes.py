from flask import request, session

from app.api import *

class Routes:
    VIEWS = [
        PostsApi,
    ]

    METHOD_DEFAULTS = {
        'index': { 'methods': ['GET'] },
        'show': { 'methods': ['GET'] },
        'create': { 'methods': ['POST'] },
        'update': { 'methods': ['PUT', 'PATCH'] },
        'delete': { 'methods': ['DELETE'] }
        }

    @classmethod
    def init_app(cls, app):
        for view in cls.VIEWS:
            view_instance = view()
            for route in view.ROUTES:
                func = getattr(view_instance, route['function'], None)
                if func:
                    route_keys = route.keys()

                    if 'kwargs' in route_keys:
                        options = route['kwargs']
                    else:
                        options = cls.METHOD_DEFAULTS.get( route['function'], {'methods': ['GET']} )

                    # if 'skip_auth' not in route_keys:
                        # func = cls.auth_handler(func)

                    app.add_url_rule(
                        route['url'],
                        f"{route['url']}#{route['function']}",
                        func,
                        **options
                    )

    # def auth_handler(self, func):
        # def new_func():
            # token = request.headers.get('Authorization', '').replace('Bearer ', '')
            # if token:
                # auth = JWT(data=token).decode()
                # if auth.get('id') and auth.get('email'):
                    # user = User.query.filter(
                        # User.id    == auth['id'],
                        # User.email == auth['email']
                    # ).one_or_none()
                    # if user:
                        # session['user'] = user.to_dict_except(keys={'encrypted_password'})
                        # return func()
            # return {'error': 'Unauthorized'}, 401
        # return new_func
