'''
@author: chenhuixi
@file: threading_poll
@time: 2021/1/14 2:25 下午
@desc: 
@Software: PyCharm
'''
"""
使用python的Thread类的子类Timer，该子类可控制指定函数在特定时间后执行一次:
所以为了实现多次定时执行某函数，只需要在一个while循环中多次新建Timer即可。
"""
from threading import Timer
import time


def printHello():
    print("Hello")
    print("当前时间戳是", time.time())


def loop_func(func, second):
    # 每隔second秒执行func函数
    while True:
        timer = Timer(second, func)
        timer.start()
        timer.join()


loop_func(printHello, 1)
