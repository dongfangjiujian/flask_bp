开始使用blueprint构建网站框架

run.py 内用应用工厂来初始化一个app  #app =create_app()
create_app类在app包的__init__.py里面
__init__.py内还需要注册blueprint

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)
    
from app.main import bp as main_bp
app.register_blueprint(main_bp)

每一个单独的包内__init__.py 需要初始化bluep
from flask import Blueprint

bp = Blueprint('main',__name__)

from app.main import  routes
---------------------------------------------
routes里app.route 变成bp.route
