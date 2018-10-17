# -*- coding=utf-8 -*-
__author = 'fansly'

from bluelog.blueprints.auth import auth_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
