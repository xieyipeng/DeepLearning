import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '178.128.180.92'
port = 8000
s.connect((host, port))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input('>>>>>>>>')  # post|11.png
    cmd, path = inp.split('|')  # 拿到post，以及文件11.jpg
    path = os.path.join(BASE_DIR, path)
    filename = os.path.basename(path)
    file_size = os.stat(path).st_size
    file_info = 'post|%s|%s' % (filename, file_size)  # split获取字符串的信息       以此方式打包，依次为   cmd/name/size
    s.sendall(bytes(file_info, 'utf8'))  # 第一次发送请求，不是具体内容，而是先发送数据信息

    f = open(path, 'rb')
    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        s.sendall(data)  # 发送真实数据
        has_sent += len(data)

    f.close()
    print('上传成功')
    msg = s.recv(1024)
    print(msg.decode('utf-8'))

# https://blog.csdn.net/liuqiangkaiduyaqian/article/details/52950068