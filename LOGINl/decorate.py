# -*- coding: utf-8 -*-
""" 
@Time:        2023/4/10 11:10
@Author:      CookieYang
@FileName:    decorate.py
@SoftWare:    PyCharm
@brief:       装饰器
"""
from functools import wraps


def permission_required(permission):
    """返回装饰器，装饰器中使用入参 permission
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not permission:
                print('403')
                return
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required_true(f):
    """装饰器函数，返回装饰器
    """
    return permission_required(True)(f)


def admin_required_false(f):
    """装饰器函数，返回装饰器
    """
    return permission_required(False)(f)


@admin_required_true
def foo():
    """使用装饰器
    """
    print('foo')


@admin_required_false
def bar():
    """使用装饰器
    """
    print('bar')


foo()
bar()
