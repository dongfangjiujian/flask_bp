from flask import render_template,redirect,url_for
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return 'hello'