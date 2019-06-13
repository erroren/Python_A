import socket
from threading import Thread
import time


def send_message(client, addr):
    while True:
        str = input("请输入要发送的消息:")
        client.sendto(str.encode("utf8"), addr)
        print("发送成功")
        time.sleep(10)


def recv_message(client, BUFFER_SIZE):
    time.sleep(2)
    while True:
        res, addr = client.recvfrom(BUFFER_SIZE)
        print("收到端口号%s消息:%s"%(addr[1], res.decode("utf8")))


if __name__ == '__main__':
    ADDR = ("192.168.12.155", 50000)
    BUFFER_SIZE = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    t1 = Thread(target=send_message, args=(client, ADDR))
    t1.start()
    t2 = Thread(target=recv_message, args=(client, BUFFER_SIZE))
    t2.start()
    t1.join()
    t2.join()
    client.close()
