# -*- coding: utf-8 -*-
__author__ = 'fansly'

@admin_bp.route('/post/manage')
@login_required
def manage_post():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).panginate(
        page, per_page=current_app.config['CRYPTICLOG_MANAGE_POST_PER_PAGE'])
    posts = pagination.items
    return render_template('admin/manage_post.html', pagination=pagination, posts=posts)
