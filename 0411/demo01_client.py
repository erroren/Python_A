from socket import *


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('192.168.12.155', 6666))
    str1 = input("输入要发送的消息:").encode("gbk")
    client.send(str1)
    print("发送成功")
    while True:
       res = client.recv(1024)
       print("收到服务器消息:%s"%res.decode("gbk"))
