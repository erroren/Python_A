from socket import *

if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("192.168.12.155", 8888))
    server.listen()
    users = []
    while True:
        client, addr = server.accept()
        print(client.name)
        users.append(addr)
        print("当前用户", users)
