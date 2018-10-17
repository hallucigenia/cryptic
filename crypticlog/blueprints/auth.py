# -*- coding: utf-8 -*-
__author__ = 'fansly'

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():

@auth_bp.route('/logout')
def logout():


