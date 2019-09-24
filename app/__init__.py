import logging
import os
from flask import Flask, request
from flask_migrate import Migrate
from config import Config
from app.routes import Routes
from db import db

migrate = Migrate()

def build_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.logger.setLevel(logging.DEBUG)

    db.init_app(app)
    migrate.init_app(app, db)
    Routes.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello!\n'

    @app.errorhandler(405)
    def method_not_allowed(e):
        return {'error': 'The method is not allowed for the requested URL.'}, 405

    return app
