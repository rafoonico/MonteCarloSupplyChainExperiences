from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_dir = os.path.join(base_dir, 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config['SECRET_KEY'] = 'change-me'

    from . import routes
    app.register_blueprint(routes.bp)

    return app