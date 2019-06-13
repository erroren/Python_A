from threading import Thread
import socket
import time

ADDR_TO = ('127.0.0.1', 60000)
BUFFER_SIZE = 1024

Clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Clientsocket.sendto("hekl".encode("utf8"), ADDR_TO)
