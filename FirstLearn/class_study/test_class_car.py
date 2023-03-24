# -*- coding: utf-8 -*-
""" 
@Time:        2022/10/25 16:17
@Author:      YangRudan
@FileName:    test_class_car.py
@SoftWare:    PyCharm
"""

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """"初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        """"返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程信息"""
        print(f"This car has {self.odometer_reading} miles on it.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性
           再初始化电动汽车的特有属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """"描述电动汽车的电池属性"""
        print(f"This car has a {self.battery_size} KWh battery.")

class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size = 75):
       """初始化电瓶的属性"""
       self.battery_size = battery_size

    def describe_battery(self):
        print(f"This electric car has a {self.battery_size} battery~")

    def get_range(self):
        """打印一条信息，指出电瓶的续驶里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go {range} miles on a full charge")

# my_tesla = ElectricCar('tesla', 'model_s', 2019)
# print(my_tesla.get_description_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()