'''
@author: chenhuixi
@file: resp_gevent
@time: 2021/1/14 4:38 下午
@desc: 
@Software: PyCharm
'''
"""
手动使用gevent配合requests模块
"""
# coding:utf-8
import gevent
import time
from gevent import monkey
import requests

monkey.patch_all()

datali = [x for x in range(50)]
task = []


def func(i):
    print(u'第{}个请求'.format(i))
    url = "http://hao.jobbole.com/python-docx/"
    resp = requests.get(url=url)
    return resp


time1 = time.time()
for i in datali:
    task.append(gevent.spawn(func, i))
res = gevent.joinall(task)
print(len(res))
time2 = time.time()
T = time2 - time1
print(T)
