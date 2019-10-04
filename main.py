from flask import Flask
from flask_cors import CORS
from app import Routes
from conf.config import APP_SETTINGS
from middleware import Database as DBMiddleware

app = Flask(__name__)
app.secret_key = APP_SETTINGS.get('secret_key', 'S0MEr4nd0mK3Y')

CORS(app)
DBMiddleware()

@app.errorhandler(405)
def method_not_allowed(e):
    return {'error': 'Method is not allowed for the requested URL.'}, 405

if __name__ == '__main__':
    # app.wsgi_app = DBMiddleware(app.wsgi_app)
    Routes(app).add_routes()
    if APP_SETTINGS['environment'] == 'production':
        from wsgiref import simple_server
        httpd = simple_server.make_server('127.0.0.1', 5000, app)
        httpd.serve_forever()
    else:
        app.run(debug=True)
