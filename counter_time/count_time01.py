# -*- coding: utf-8 -*-
""" 
@Time:        2023/5/29 14:36
@Author:      CookieYang
@FileName:    count_time01.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        name = func
        for attr in ('__qualname__', '__name__'):
            if hasattr(func, attr):
                name = getattr(func, attr)
                break

        print("Start call: {}".format(name))
        now = time.time()
        result = func(*args, **kwargs)
        using = (time.time() - now) * 1000
        msg = "End call {}, using: {:.1f}ms".format(name, using)
        print(msg)
        return result

    return wrapper


@timeit
def hello_world():
    time.sleep(2)
    print('hello world')


if __name__ == '__main__':
    hello_world()