# -*- coding: utf-8 -*-
""" 
@Time:        2023/7/17 10:08
@Author:      CookieYang
@FileName:    first_pyside.py
@SoftWare:    PyCharm
@brief:       功能简介
"""
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QLabel

# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
label = QLabel("Hello World")
label.show()
# Enter Qt application main loop
app.exec_()
sys.exit()
