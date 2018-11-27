# -*- coding: utf-8 -*-
__author__ = 'fansly'

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_whooshee import Whooshee
from flask_qiniustorage import Qiniu
from flask_caching import Cache
from redis import Redis

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()
moment = Moment()
toolbar = DebugToolbarExtension()
migrate = Migrate()
whooshee = Whooshee()
qiniu_store = Qiniu()
redis = Redis()
cache = Cache(config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'fcache',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': '6379',
    'CACHE_REDIS_URL': 'redis://localhost:6379'
    })


@login_manager.user_loader
def load_user(user_id):
    from cryptic.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
# login_manager.login_message = "Your custom message"
login_manager.login_message_category = 'warning'
