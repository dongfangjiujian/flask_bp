from flask import Flask,current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import  Migrate
from flask_bootstrap import Bootstrap

# 首先实例化 但不馋参数
db = SQLAlchemy()
migrate = Migrate()
# login的一系列设置
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = '请先登录'
bootstrap = Bootstrap()

# 应用工厂
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    bootstrap.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import  models