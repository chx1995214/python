'''
@author: chenhuixi
@file: threading
@time: 2021/1/14 11:30 上午
@desc: 
@Software: PyCharm
'''
import threading

import operator
import csv
import time
import threading
from time import ctime

# 乱序多线程写入
import threading


def write_string(string, path="test.csv"):
    with open(path, 'a') as f:
        f.write(string + "\r\n")


# 创建新线程
for i in range(15):
    # 这里每次循环都开一个线程，并写入"写入:" + i，args里指定参数，注意要使用list[]格式
    thread1 = threading.Thread(target=write_string, args=["写入: " + str(i)])
    thread1.start()

# 正序多线程写入
threadLock = threading.Lock()


def write_string(string, path="test.csv"):
    threadLock.acquire()  # 加个同步锁就好了
    with open(path, 'a') as f:
        f.write(string + "\r\n")
    threadLock.release()


# 创建新线程
for i in range(15):
    thread1 = threading.Thread(target=write_string, args=["写入: " + str(i)])
