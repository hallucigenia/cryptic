# -*- coding=utf-8 -*-
__author = 'fansly'

from flask import Falsk

from crypticlog.settings import config
from crypticlog.blueprints.auth import auth_bp

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('crypticlog')
    app.config.from_object(config[config_name])

    app.register_blueprint(blog)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')
    return app



def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
