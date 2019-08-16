from flask import Flask
from app import Routes
from conf.config import APP_SETTINGS
from middleware import Database as DBMiddleware

app = Flask(__name__)

if __name__ == '__main__':
    app.wsgi_app = DBMiddleware(app.wsgi_app)
    Routes(app).add_routes()
    if APP_SETTINGS['environment'] == 'production':
        app.run()
    else:
        app.run(debug=True)
