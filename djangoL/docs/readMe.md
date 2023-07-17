# Django入门

## 建立虚拟环境

~~~
python -m venv ll_env
source ll_env/bin/activate  (linux)
.\ll_env\Scripts\activate (windows)
deactivate  //停止使用虚拟环境
~~~

## 安装Django

~~~
pip install django
~~~

## 在Django中创建项目
注意命令最后这个.
~~~
django-admin startproject learning_log . 
~~~

## 创建数据库

~~~
python .\manage.py migrate   
~~~

## 查看项目

~~~
python .\manage.py runserver   
~~~

## 创建应用程序

~~~
python .\manage.py startapp learning_logs
~~~


## 定义模型-激活模型-注册模型（code_intro。md)