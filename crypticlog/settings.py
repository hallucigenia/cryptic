# -*- coding=utf-8 -*-
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
    MAIL_DEFAULT_SENDER = ('Crypticlog Admin', MAIL_USERNAME)

    CRYPTICLOG_EMAIL = os.getenv('CRYPTICLOG_EMAIL')
    CRYPTICLOG_POST_PER_PAGE = 10
    CRYPTICLOG_MANAGE_POST_PER_PAGE = 15
    CRYPTICLOG_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    CRYPTICLOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    CRYPTICLOG_SLOW_QUERY_THRESHOLD = 1


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
