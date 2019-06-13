from threading import Thread
import socket
import time

ADDR_TO = ('192.168.12.155', 60000)
BUFFER_SIZE = 1024


def send_message(Clientsocket):
    while True:
       str = input("请输入消息:")
       Clientsocket.sendto(str.encode("utf8"), ADDR_TO)
       time.sleep(10)


def recv_message(Clientsocket):
    time.sleep(2)
    while True:
        message, addr = Clientsocket.recvfrom(BUFFER_SIZE)
        if message:
            print("收到消息:", message.decode("utf8"))


if __name__ == '__main__':
    Clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Clientsocket.sendto("aa".encode("utf8"), ADDR_TO)
    t1 = Thread(target=send_message, args=(Clientsocket,))
    t2 = Thread(target=recv_message, args=(Clientsocket,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    Clientsocket.close()
