# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/11 9:57
@Author:      CookieYang
@FileName:    myapp.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
from flask import Flask, make_response, render_template, session
from flask_restful import Resource, Api
from flask_wtf import csrf, Form
from wtforms import SubmitField

app = Flask(__name__)
app.secret_key = '5accdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e'
api = Api(app)

num_elements_to_generate = 500

class HelloForm(Form):
    submit_button = SubmitField('Submit This Form')

class Hello(Resource):
    def check_session(self):
        if session.get('big'):
            message = "session['big'] contains {} elements<br>".format(len(session['big']))
        else:
            message = "There is no session['big'] set<br>"
        message += "session['secret'] is {}<br>".format(session.get('secret'))
        message += "session['csrf_token'] is {}<br>".format(session.get('csrf_token'))
        return message

    def get(self):
        myform = HelloForm()
        session['big'] = list(range(num_elements_to_generate))
        session['secret'] = "A secret phrase!"
        csrf.generate_csrf()
        message = self.check_session()
        return make_response(render_template("hello.html", message=message, form=myform), 200, {'Content-Type': 'text/html'})

    def post(self):
        csrf.generate_csrf()
        message = self.check_session()
        return make_response("<p>This is the POST result page</p>" + message, 200, {'Content-Type': 'text/html'})

api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True)