# -*- coding: utf-8 -*-
""" 
@Time:        2022/12/13 15:44
@Author:      CookieYang
@FileName:    uitl.py
@SoftWare:    PyCharm
@brief:       生成验证码功能
"""
import random
from PIL import Image, ImageFont, ImageDraw

#自定义get_color方法，获取三位随机数并保存在元组中
def get_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#自定义generate_image方法绘制图片验证码
def generate_image(4):
    size=(130,50)       #设置验证码的大小
    im=Image.new('RGB',size,color=get_random_color()) #创建验证码背景图
    font=ImageFont.truetype('C:\Windows\Fonts/simsun.ttc',size=40) #设置验证码字体
    draw=ImageDraw.Draw(im)    #创建ImageDraw对象
    code=''    #设置验证码值
    s='abcdefghijklmnopqrstuvwxyz123456'  #设置验证码的取值范围
    for i in range(4):      #绘制4位数验证码值
        c=random.choice(s)   #随机在s中取值
        code+=c      #将取到的值放在验证码中
        draw.text((9+random.randint(4,7)+20*i,random.randint(4,7)),text=c,fill=get_random_color(),font=font) #在验证码背景图中写入验证码值
    im.show()
    return im ,code    #返回图片和验证码值