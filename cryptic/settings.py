# -*- coding: utf-8 -*-
__author__ = 'fansly'

import os
import sys


prefix = 'mysql+pymysql://root:950419@localhost/'

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Cryptic Admin', MAIL_USERNAME)

    CRYPTIC_EMAIL = os.getenv('CRYPTIC_EMAIL')
    CRYPTIC_POST_PER_PAGE = 10
    CRYPTIC_MANAGE_POST_PER_PAGE = 15
    CRYPTIC_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    CRYPTIC_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    CRYPTIC_SLOW_QUERY_THRESHOLD = 1

    QINIU_ACCESS_KEY = os.getenv('ACCESS_KEY')
    QINIU_SECRET_KEY = os.getenv('SECRET_KEY')
    QINIU_BUCKET_NAME = 'pre-nectarian'
    QINIU_BUCKET_DOMAIN = 'pifzqj4jd.bkt.clouddn.com'

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:950419@localhost/tea'


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:950419@localhost/tea'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + 'tea')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
