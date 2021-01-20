'''
@author: chenhuixi
@file: threading_lession3
@time: 2021/1/14 2:14 下午
@desc: 
@Software: PyCharm
'''
import time
from threading import Thread


def add():
    sum = 0
    i = 1
    while i <= 1000000:
        sum += i
        i += 1
    print('sum:', sum)


def mul():
    sum2 = 1
    i = 1
    while i <= 100000:
        sum2 = sum2 * i
        i += 1
    print('sum2:', sum2)


start = time.time()

add()
mul()  # 串行比多线程还快

print('cost time %s' % (time.time() - start))
