from socket import *
from threading import Thread
import time


def sendmessage(client):
    while True:
        try:
            if not client._closed:
                str1 = input("输入消息").encode("utf8")
                if client._closed:
                    break
                else:
                    client.send(str1)
                    print("发送成功")
                    time.sleep(2)
            else:
                break
        except Exception as e:
            print(e)


def recvmessage(client):
    while True:
        try:
            res = client.recv(1024)
            if len(res) > 0:
                print("收到服务端消息%s" % res.decode("utf8"))
            else:

                client.close()
                break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("192.168.12.155", 8888))
    t1 = Thread(target=sendmessage, args=(client,))
    t1.start()
    t2 = Thread(target=recvmessage, args=(client,))
    t2.start()
    t1.join()
    t2.join()
    print("服务器已关闭，自动退出")


