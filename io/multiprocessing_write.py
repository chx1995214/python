'''
@author: chenhuixi
@file: multiprocessing_write
@time: 2021/1/14 11:42 上午
@desc: 
@Software: PyCharm
'''
# coding:utf-8
import os
import re
from multiprocessing import Pool
import time


def mycallback(x):
    with open('123.txt', 'a+') as f:
        f.writelines(str(x))


def sayHi(num):
    return num


if __name__ == '__main__':
    e1 = time.time()
    pool = Pool()

    for i in range(10):
        pool.apply_async(sayHi, (i,), callback=mycallback)

    pool.close()
    pool.join()
    e2 = time.time()
    print
    float(e2 - e1)
