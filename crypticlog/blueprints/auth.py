# -*- coding: utf-8 -*-
__author__ = 'fansly'

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from crypticlog.models import Admin
from crypticlog.forms import LoginForm
from crypticlog.utils import redirect_back

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            # verify username and password
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)  # login user
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login-page.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()
