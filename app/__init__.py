# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_pyfile('config.py')

    # Register blueprints
    from app.api.routes import api_bp
    app.register_blueprint(api_bp)

    return app