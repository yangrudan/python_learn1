# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/10 17:43
@Author:      CookieYang
@FileName:    demo.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
# coding:utf-8

from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField  # 导入字段类型
from wtforms.validators import DataRequired, EqualTo  # 导入验证器

app = Flask(__name__)

# CSRF_ENABLED是为了CSRF（跨站请求伪造）保护。 SECRET_KEY用来生成加密令牌，当CSRF激活的时候，该设置会根据设置的密匙生成加密令牌。
app.config["SECRET_KEY"] = "xhosd6f982yfhowefy29f"  # 使用Flask-WTF需要配置参数SECRET_KEY (csrf)


# 定义表单的模型类 (一个类属性对应表单一个input标签)
class RegisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    # 在前端模板中可以通过label参数获取该input标签的说明信息。 validators参数表示验证器
    # DataRequired 保证数据必须填写，并且不能为空
    user_name = StringField(label=u"用户名", validators=[DataRequired(u"用户名不能为空")])  # 通过validators来指定前端表单数据的校验。
    password = PasswordField(label=u"密码", validators=[DataRequired(u"密码不能为空")])
    password2 = PasswordField(label=u"确认密码", validators=[DataRequired(u"确认密码不能为空"),
                                                             EqualTo("password", u"两次密码不一致")])
    submit = SubmitField(label=u"提交")


@app.route("/show_register")
def show_register():
    # 创建表单对象。
    form = RegisterForm()

    return render_template("register.html", form=form)  # 将form模板变量分配给模板


@app.route("/register", methods=["POST"])
def register():
    # 创建表单对象。 如果是post提交表单，flask会自动把表单数据封装到form对象中
    form = RegisterForm()

    # 验证form中的数据(包括csrf验证)
    # 如果form中的数据完全满足所有的验证器，则返回真，否则返回假
    if form.validate_on_submit():
        # 如果验证通过
        # 提取数据
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        session["user_name"] = uname
        return redirect(url_for("index"))

    # 如果校验未通过
    return render_template("register.html", form=form)


@app.route("/index")
def index():
    user_name = session.get("user_name", "")
    return "hello %s" % user_name


if __name__ == '__main__':
    app.run(debug=True)
