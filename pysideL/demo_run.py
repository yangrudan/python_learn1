# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/17 10:30
@Author:      CookieYang
@FileName:    demo_run.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from demo_ui import Ui_MainWindow


# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
    # 注意，在PySide6中，需要使用app.exec()
    # sys.exit(app.exec())