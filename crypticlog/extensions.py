# -*- coding: utf-8 -*-
__author__ = 'fansly'

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import sqlalchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()


@login_manager.user_loader
def load_user(user_id):
    from Crypticlog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
