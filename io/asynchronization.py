'''
@author: chenhuixi
@file: asynchronization
@time: 2021/1/14 2:48 下午
@desc: 
@Software: PyCharm
'''
import socket
import select

"""
########http请求本质，IO阻塞########
sk = socket.socket()
#1.连接
sk.connect(('www.baidu.com',80,)) #阻塞
print('连接成功了')
#2.连接成功后发送消息
sk.send(b"GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n")

#3.等待服务端响应
data = sk.recv(8096)#阻塞
print(data) #\r\n\r\n区分响应头和影响体

#关闭连接
sk.close()
"""
"""
########http请求本质，IO非阻塞########
sk = socket.socket()
sk.setblocking(False)
#1.连接
try:
    sk.connect(('www.baidu.com',80,)) #非阻塞，但会报错
    print('连接成功了')
except BlockingIOError as e:
    print(e)

#2.连接成功后发送消息
sk.send(b"GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n")

#3.等待服务端响应
data = sk.recv(8096)#阻塞
print(data) #\r\n\r\n区分响应头和影响体

#关闭连接
sk.close()
"""


class HttpRequest:
    def __init__(self, sk, host, callback):
        self.socket = sk
        self.host = host
        self.callback = callback

    def fileno(self):
        return self.socket.fileno()


class HttpResponse:
    def __init__(self, recv_data):
        self.recv_data = recv_data
        self.header_dict = {}
        self.body = None

        self.initialize()

    def initialize(self):
        headers, body = self.recv_data.split(b'\r\n\r\n', 1)
        self.body = body
        header_list = headers.split(b'\r\n')
        for h in header_list:
            h_str = str(h, encoding='utf-8')
            v = h_str.split(':', 1)
            if len(v) == 2:
                self.header_dict[v[0]] = v[1]


class AsyncRequest:
    def __init__(self):
        self.conn = []
        self.connection = []  # 用于检测是否已经连接成功

    def add_request(self, host, callback):
        try:
            sk = socket.socket()
            sk.setblocking(0)
            sk.connect((host, 80))
        except BlockingIOError as e:
            pass
        request = HttpRequest(sk, host, callback)
        self.conn.append(request)
        self.connection.append(request)

    def run(self):

        while True:
            rlist, wlist, elist = select.select(self.conn, self.connection, self.conn, 0.05)
            for w in wlist:
                print(w.host, '连接成功...')
                # 只要能循环到，表示socket和服务器端已经连接成功
                tpl = "GET / HTTP/1.0\r\nHost:%s\r\n\r\n" % (w.host,)
                w.socket.send(bytes(tpl, encoding='utf-8'))
                self.connection.remove(w)
            for r in rlist:
                # r,是HttpRequest
                recv_data = bytes()
                while True:
                    try:
                        chunck = r.socket.recv(8096)
                        recv_data += chunck
                    except Exception as e:
                        break
                response = HttpResponse(recv_data)
                r.callback(response)
                r.socket.close()
                self.conn.remove(r)
            if len(self.conn) == 0:
                break


def f1(response):
    print('保存到文件', response.header_dict)


def f2(response):
    print('保存到数据库', response.header_dict)


url_list = [
    {'host': 'www.youku.com', 'callback': f1},
    {'host': 'v.qq.com', 'callback': f2},
    {'host': 'www.cnblogs.com', 'callback': f2},
]

req = AsyncRequest()
for item in url_list:
    req.add_request(item['host'], item['callback'])

req.run()
