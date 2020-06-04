import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from time import time

from app import db
from .base import Base

class User(Base, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    encrypted_password = db.Column(db.String)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    posts = db.relationship('Post', lazy='select', backref=db.backref('author', lazy='select'))


    def set_password(self, password):
        self.encrypted_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.encrypted_password, password)

    def from_dict(self, data):
        for field in ['email']:
            if field in data:
                setattr(self, field, data[field])
        if 'password' in data:
            self.set_password(data['password'])

    def to_dict(self):
        return super().to_dict(whitelist={'id', 'email'})

    def generate_auth_token(self, expires_in=86400):
        return jwt.encode({'id': self.id, 'email': self.email, 'exp': time() + expires_in},
                'SECRET_KEY',
                algorithm='HS256').decode('utf-8')

    @staticmethod
    def find_by_token(token):
        data = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
        return User.query.get(data['id'])
