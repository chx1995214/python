'''
@author: chenhuixi
@file: threading_lession1
@time: 2021/1/14 2:07 下午
@desc: 
@Software: PyCharm
'''
import threading  # 线程
import time


def music():
    print('begin to listen music {}'.format(time.ctime()))
    time.sleep(3)
    print('stop to listen music {}'.format(time.ctime()))


def game():
    print('begin to play game {}'.format(time.ctime()))
    time.sleep(5)
    print('stop to play game {}'.format(time.ctime()))


if __name__ == '__main__':
    music()
    game()
    print('ending.....')
