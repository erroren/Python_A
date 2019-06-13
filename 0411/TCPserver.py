from threading import Thread
from socket import *
import time

BUFFERSIZE = 1024
SERVERADDR = ('192.168.12.155', 8888)


def readprocess(client, users, BUFFERSIZE):
    while True:
        res = client.recv(BUFFERSIZE)
        print(res)
        if len(res) > 0:
            res = res.decode("gbk").split(":")
            print("发送给%s的消息:%s"%(res[0], res[1]))
            for u in users:
                if u["PORT"] == int(res[0]):
                    print(u["Client"], type(u["Client"]))
                    u["Client"].send(res[1].encode("gbk"))
                    break
            else:
                client.send("该用户已下线".encode("gbk"))
            # print(client)
            # str1 = input("回复消息:").encode("utf8")
            # print(res)
            # client.send(str1)
            # time.sleep(2)
            # print("发送成功")
def listen(serversocket,users):
    while True:
        clientsocket, addr = serversocket.accept()
        user = {"IP": addr[0], "PORT": addr[1], "Client": clientsocket}
        users.append(user)
        print("当前用户数%d" % len(users))
        print(users)
        p1 = Thread(target=readprocess, args=(clientsocket, users, BUFFERSIZE))
        p1.start()


if __name__ == '__main__':
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind(SERVERADDR)
    serversocket.listen(100)
    users = []
    t1 = Thread(target=listen, args=(serversocket, users))
    t1.start()
    # while True:
    #     postnum = input("发送用户端口号:")
    #     message = input("发送的消息").encode("utf8")
    #     for u in users:
    #         if u["PORT"] == int(postnum):
    #             print(u["Client"])
    #             u["Client"].send(message)
    #             print("发送成功")
