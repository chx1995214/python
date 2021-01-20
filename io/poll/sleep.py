'''
@author: chenhuixi
@file: sleep
@time: 2021/1/14 2:27 下午
@desc: 
@Software: PyCharm
'''
"""
使用time模块的sleep函数可以阻塞程序执行,
这种更节约资源，因为同样使用了while循环，没有生成多余的线程。
"""

import time


def printHello():
    print("Hello")
    print("当前时间戳是", time.time())


def loop_func(func, second):
    # 每隔second秒执行func函数
    while True:
        func()
        time.sleep(second)


loop_func(printHello, 1)
