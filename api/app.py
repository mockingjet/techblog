from flask import Flask
from flask_cors import CORS
from conf import Config
from db import db
from urls import api
import click


def create_app(config=Config):
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config)

    db.init_app(app)
    api.init_app(app)

    @app.route('/')
    def test():
        db.create_all()
        return 'test'

    return app
