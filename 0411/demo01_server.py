from socket import *


if __name__ == '__main__':
    SERVERADDR = ('192.168.12.155', 6666)
    SIZE = 1024
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(SERVERADDR)
    server.listen()
    while True:
        client, addr = server.accept()
        print("%s已上线"%(addr[1]))
        while True:
            res = client.recv(SIZE)
            if len(res) > 0:
                print("接收到%s的消息:%s"%(addr[1], res.decode("gbk")))
                str1 = input("输入回复消息:").encode("gbk")
                client.send(str1)
            else:
                print("%s已断开连接"%(addr[1]))
                client.close()
                break
