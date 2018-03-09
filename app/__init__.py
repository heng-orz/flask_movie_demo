# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.debug = True
'''
用于连接数据的数据库。例如：

sqlite:////tmp/test.db
mysql://username:password@server/db
'''
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/movie";
'''
如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
'''
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)



from app.home import home as  home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
