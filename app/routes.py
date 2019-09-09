from flask import request, session

import sqlalchemy
from conf.database import db_session

from app.api import Home
from app.model import User
from app.service import JwtService as JWT
from conf.config import METHOD_DEFAULTS
from conf.config import METHOD_DEFAULTS

class Routes:
    VIEWS = [
        Home,
    ]

    def __init__(self, instance):
        self.instance = instance

    def add_routes(self):
        for view in self.VIEWS:
            view_instance = view()
            for route in view.ROUTES:
                func = getattr(view_instance, route['function'], None)
                if func:
                    route_keys = route.keys()

                    if 'kwargs' in route_keys:
                        options = route['kwargs']
                    else:
                        options = METHOD_DEFAULTS.get( route['function'], {'methods': ['GET']} )

                    if 'skip_auth' not in route_keys:
                        func = self.auth_handler(func)

                    self.instance.add_url_rule(
                        route['url'],
                        f"{route['url']}#{route['function']}",
                        func,
                        **options
                    )

    def auth_handler(self, func):
        def new_func():
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if token:
                auth = JWT(data=token).decode()
                if auth.get('id') and auth.get('email'):
                    user = User.query.filter(
                        User.id    == auth['id'],
                        User.email == auth['email']
                    ).one_or_none()
                    if user:
                        session['user'] = user.to_dict_except(keys={'encrypted_password'})
                        return func()
            return {'error': 'Unauthorized'}, 401
        return new_func

