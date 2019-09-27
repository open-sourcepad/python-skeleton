import logging
from flask import Flask, request
from flask_migrate import Migrate

from app import app, db
from routes import Routes

Migrate().init_app(app, db)
Routes.init_app(app)

app.logger.setLevel(logging.DEBUG)

@app.errorhandler(405)
def method_not_allowed(e):
    return {'error': 'The method is not allowed for the requested URL.'}, 405
