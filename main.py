from flask import Flask, jsonify
from app import Routes
from conf.config import APP_SETTINGS
from middleware import Database as DBMiddleware

app = Flask(__name__)

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'The method is not allowed for the requested URL.'}), 405

DBMiddleware()

if __name__ == '__main__':
    # app.wsgi_app = DBMiddleware(app.wsgi_app)
    Routes(app).add_routes()
    if APP_SETTINGS['environment'] == 'production':
        app.run()
    else:
        app.run(debug=True)
