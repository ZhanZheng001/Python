from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
#sqlalchemy配置
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://root:123456@127.0.0.1/daxiong')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

from app import routes