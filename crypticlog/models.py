# -*- coding: utf-8 -*-
__author__ = 'fansly'

from datetime import datetime
from crypticlog.extensions import db

class Admin(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DataTime, default=datetime.utcnow)
