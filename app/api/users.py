from flask import request, session
from app.models import User

from .base import Base

class UsersApi(Base):
    ROUTES = [
        { 'url': '/register', 'function': 'register', 'methods': ['POST'], 'skip_auth': True },
        { 'url': '/login', 'function': 'login', 'methods': ['POST'], 'skip_auth': True },
        ]


    def register(self, **kwargs):
        params = request.get_json()

        errors = self._validate_register(params)
        if errors:
            return {'errors': errors}, 422

        obj = User()
        obj.from_dict(params)
        obj.save()

        if obj.id is None:
            return {'error': 'Something went wrong'}, 422

        data = self._get_session_info(obj)
        return self._to_json(data), 201


    def login(self, **kwargs):
        params = request.get_json()
        obj = User.query.filter(User.email==params['email']).first()
        if obj and obj.check_password(params['password']):
            return self._get_session_info(obj)
        return {'error': 'Invalid credentials'}, 401


    def _get_session_info(self, obj):
        data = obj.to_dict()
        data['auth_token'] = obj.generate_auth_token()
        return data

    def _validate_register(self, fields):
        errors = []

        email = fields.get('email')
        if email is None or email == '':
            errors.append('Email must be provided')
        elif email:
            exists = User.query.filter(User.email == email).count() > 0
            if exists:
                errors.append('Email is already in use')

        password = fields.get('password')
        if password is None or password == '':
            errors.append('Password must be provided')

        if len(errors) > 0:
            return errors
