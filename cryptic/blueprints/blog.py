# -*- coding: utf-8 -*-
__author__ = 'fansly'

import time
from flask import Flask, render_template, Blueprint, request, abort, make_response, flash, redirect, url_for, current_app, send_from_directory
from flask_login import current_user
from cryptic.models import Comment, Post, Category
from cryptic.extensions import db, cache
from cryptic.forms import AdminCommentForm, CommentForm
from cryptic.emails import send_new_comment_email, send_new_reply_email
from cryptic.utils import redirect_back

blog_bp = Blueprint('blog', __name__, static_folder='../static')
 

@blog_bp.route('/robots.txt')
@blog_bp.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(blog_bp.static_folder, request.path[1:])


@blog_bp.route('/')
@cache.cached(timeout= 20 * 60)
def index():
    time.sleep(1)
    page = request.args.get('page', 1, type=int)  # git current page during searching string
    per_page = current_app.config['CRYPTIC_POST_PER_PAGE']  # page count
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)  # paging objects
    posts = pagination.items  # current page's record list
    return render_template('blog/index.html', pagination=pagination, posts=posts)


@blog_bp.route('/about')
@cache.cached(timeout=30 * 60)
def about():
    time.sleep(1)
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['CRYPTIC_POST_PER_PAGE']
    pagination = Post.query.with_parent(category).order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/category.html', category=category, pagination=pagination, posts=posts)

def make_cache_key(*args, **kwargs):
    """Dynamic creation the request url."""

    path = request.path
    args = str(hash(frozenset(request.args.items())))
    return (path + args).encode('utf-8')


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
@cache.cached(timeout=10 * 60) 
def show_post(post_id):
    time.sleep(1)
    post = Post.query.get_or_404(post_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['CRYPTIC_COMMENT_PER_PAGE']
    pagination = Comment.query.with_parent(post).filter_by(
        reviewed=True).order_by(
        Comment.timestamp.asc()).paginate(
            page,
        per_page)
    comments = pagination.items

    if current_user.is_authenticated:  # if current user logined, use the administrator form
        form = AdminCommentForm()
        form.author.data = current_user.name
        form.email.data = current_app.config['CRYPTIC_EMAIL']
        form.site.data = url_for('.index')
        from_admin = True
        reviewed = True
    else:  # if not login, use comment form
        form = CommentForm()
        from_admin = False
        reviewed = False

    if form.validate_on_submit():
        author = form.author.data
        email = form.email.data
        site = form.site.data
        body = form.body.data
        comment = Comment(
            author=author, email=email, site=site, body=body,
            from_admin=from_admin, post=post, reviewed=reviewed)
        replied_id = request.args.get('reply')
        if replied_id:  # if 'reply'exist in URL, that mains reply
            replied_comment = Comment.query.get_or_404(replied_id)
            comment.replied = replied_comment
            send_new_reply_email(replied_comment)  # send email to replyed user
        db.session.add(comment)
        db.session.commit()
        if current_user.is_authenticated:  # show different alarm according to different login status
            flash('Comment published.', 'success')
        else:
            flash('Thanks, your comment will be published after reviewed.', 'info')
            send_new_comment_email(post)  # send remind mail to admin
        return redirect(url_for('.show_post', post_id=post_id))
    return render_template('blog/post.html', post=post, pagination=pagination, form=form, comments=comments)


@blog_bp.route('/reply/comment/<int:comment_id>')
def reply_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if not comment.post.can_comment:
        flash('Comment is disabled.', 'warning')
        return redirect(url_for('.show_post', post_id=comment.post.id))
    return redirect(
        url_for(
            '.show_post',
            post_id=comment.post_id,
            reply=comment_id,
            author=comment.author) +
        '#comment-form')


@blog_bp.route('/search')
def search():
    q = request.args.get('q', '')
    if q == '':
        flash('Enter keyword about post .', 'warning')
        return redirect_back()

    category = request.args.get('category', 'photo')
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['ALBUMY_SEARCH_RESULT_PER_PAGE']
    pagination = Post.query.whooshee_search(q).paginate(page, per_page)
    results = pagination.items
    return render_template('blog/search.html', q=q, results=results, pagination=pagination, category=category)