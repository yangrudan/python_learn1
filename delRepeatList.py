# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/22 9:49
@Author:      CookieYang
@FileName:    delRepeatList.py
@SoftWare:    PyCharm
@brief:       功能简介 删除列表中重复元素
"""

'''方法一'''
def dedup(items):
    no_dup_items = []
    seen = set()
    for item in items:
        if item not in seen:
            no_dup_items.append(item)
            seen.add(item)
    print(seen)
    return no_dup_items


'''方法二'''
def dedup2(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    print(seen)

def demo():
    myList = [7,1,1,2,3,4,5,4]
    print(len(myList))

    res = dedup2(myList)
    #print(len(res))


if __name__ == '__main__':
    demo()