# -*- coding: utf-8 -*-
""" 
@Time:        2023/3/29 10:28
@Author:      CookieYang
@FileName:    no_problem.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import tornado.ioloop
import tornado.web

html = """
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>GRP Demo</title> 
</head>
<body>

<form name="input" action="submit" method="post">
    提交的内容: <input type="text" name="submit-content">
    <br>
    <input type="submit" value="提交">
</form>

</body>
</html>
"""


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish(html)


class SubmitHandler(tornado.web.RequestHandler):

    def get(self):
        self.finish(f'提交成功')

    def post(self):
        submit_content = self.get_body_argument('submit-content')
        print(f'Receive submit: {submit_content}')
        self.redirect('submit_success')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/submit', SubmitHandler),
        (r'/submit_success', SubmitHandler),
    ], autoreload=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('Visit http://127.0.0.1:8888')
    tornado.ioloop.IOLoop.current().start()