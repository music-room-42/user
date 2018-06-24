from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def configure_app(app: Flask):
    env_name = os.getenv('ENV', 'development').lower().capitalize()
    app.config.from_object(f'user.config.{env_name}Config')


def init_app():
    app = Flask(__name__)
    configure_app(app)
    db.init_app(app)

    from .users import users_blueprint
    app.register_blueprint(users_blueprint)

    return app


app = init_app()
