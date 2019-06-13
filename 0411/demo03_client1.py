from socket import *
from threading import Thread


def send_message(client,name):
    while True:
        choice = int(input("请选择发送类型（1.私聊 2所有人）："))
        res = input("请输入消息(格式：端口号-消息）:")
        if choice == 1:
            res = res+"-1-"+name
            client.send(res.encode("gbk"))
        else:
            res = res+"-2-"+name
            client.send(res.encode("gbk"))


def recv_message(client):
    while True:
        res = client.recv(1024)
        print(res.decode("gbk"))


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('192.168.12.155', 6666))
    name = input("请输入昵称:")
    t1 = Thread(target=send_message, args=(client, name))
    t1.start()
    t2 = Thread(target=recv_message, args=(client,))
    t2.start()
    t1.join()
    t2.join()