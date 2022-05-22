from flask import Flask,url_for,render_template,request
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate
from flask_script import Manager,Command
from collections import namedtuple

app = Flask(__name__)
app.config['SECRET_KEY']='daxiongketang'
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:123456@localhost/flask_demo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.debug=True

db=SQLAlchemy(app)
migrate = Migrate(app,db)

manager=Manager(app)
# 继承Command类
class Hello(Command):
    def run(self):
        print('Hello world')
manager.add_command('hello',Hello())

#装饰器方式添加命令
@manager.command
def hi():
    print('hi ,andy')

@manager.option('-n','--name',help = '填写name')
def hi2(name):
    print(f'hi ,{name}')

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    gender = db.Column(db.Boolean(),default=True)
    hobby=db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    articles = db.relationship('Article',backref='user')#backref反向引用
    def __repr__(self):
        return f'<User> is {self.username}'
class Article(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#外键关联user表id列
    # user = db.relationship('User')
    def __repr__(self):
        return f'<Article> is {self.title}'

@app.route('/user/<username>')
def show_user_info(username):
    return render_template('user.html',name=username)

@app.route('/test/')
def test():
    return url_for('show_user_info',username='andy')

# class User():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         return f'我的名字是{self.name},年龄{self.age}'

@app.route('/')
def index():
    dict_val = {'name':'andy','age':18}
    list_val = [i for i in range(10)]
    User = namedtuple('User','name age')
    user = User('andy',18)
    return render_template('index.html',info=dict_val,number= list_val,user=user)

@app.route('/post/<int:post_id>')
def show_post_info(post_id):
    return f'post_id是{post_id}'

@app.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    # if request.method == 'POST' and form.validate():
    if form.validate_on_submit():
        pass
    return render_template('login.html',form=form)

if __name__ == '__main__':
    # app.run(port=8000,debug=True)
    # db.create_all()
    manager.run()