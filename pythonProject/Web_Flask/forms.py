from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,data_required
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField(label='用户名',validators=[
        data_required('请填写用户名'),
        Length(min=6,max=50,message='用户名长度6-50位')
    ])
    password = PasswordField(label='密码', validators=[
        data_required('请填写密码'),
        Length(min=6, max=50,message='密码长度6-50位')
    ])
    submit = SubmitField(label='提交')