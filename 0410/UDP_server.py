import socket
from threading import Thread


def recv_message(server, BUFFER_SIZE):
    while True:
        res, addr = server.recvfrom(BUFFER_SIZE)
        if res:
            print("收到%s的消息:%s"% (addr[1], res.decode("utf8")))
            str = input("回复消息:")
            server.sendto(str.encode("utf8"), addr)
            print("回复成功")


if __name__ == '__main__':
    ADDR = ("192.168.12.155", 50000)
    BUFFER_SIZE = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    t1 = Thread(target=recv_message, args=(server, BUFFER_SIZE))
    t1.start()
    t1.join()
    server.close()
