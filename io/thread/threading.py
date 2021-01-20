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

def read_file(filpos,i):
    with open(filpos+str(i)+".csv") as f:
        reader=csv.reader(f)
        for i in reader:
            print(i)

threads = []
x=0
for t in range(0,3):
    t= threading.Thread(target=read_file,args=("D:/zhihu/",x))
    threads.append(t)
    x+=1
#join在里面时候只有第一个子进程结束才能打开第二个进程,if__name__ 调用时不可用
if __name__=="__main__":
    for thr in threads:
        thr.start()
    thr.join()
    print("all over %s"%ctime())