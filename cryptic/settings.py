# -*- coding: utf-8 -*-
__author__ = 'fansly'

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


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

    UPLOADED_PHOTOS_DEST = '/uploads/photos'
    UPLOADED_PHOTO_DEST = '/uploads/photos'


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
