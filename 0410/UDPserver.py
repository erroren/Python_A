from threading import Thread
import socket
import time


def recv_message(serversocket):
    time.sleep(2)
    while True:
        message, addr = serversocket.recvfrom(BUFFER_SIZE)
        if message:
            print("收到消息", message.decode("utf8"))
            str = input("请输入回复消息")
            serversocket.sendto(str.encode("utf8"), addr)


if __name__ == '__main__':
    BUFFER_SIZE = 1024
    addr = ('192.168.12.155', 60000)
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serversocket.bind(addr)
    t1 = Thread(target=recv_message,args=(serversocket,))
    t1.start()
    t1.join()
    serversocket.close()
