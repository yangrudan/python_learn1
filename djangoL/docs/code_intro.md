## 定义模型
（ps： logging_logs下的admin.py、model.py、view.py很重要）

修改model.py

## 激活模型

1. 在logging_log的setting.py加入INSTALLED_APPS；

2. 迁徙 python .\manage.py makemigrations learning_logs  ；

3. python .\manage.py migrate

## 注册模型

admin.py下register

## Django shell调试
~~~
python .\manage.py shell
~~~

## 映射url(urls.py) - 编写视图（view.py） - 创建模板（html)