from socket import *
from threading import Thread


def get_and_send(client, users, user):
    while True:
        res = client.recv(1024)
        print(res.decode("gbk"))
        if len(res) > 0:
            res = res.decode("gbk").split("-")
            print(res)
            if res[-2] == "1":
                print("%s发送给%s的消息%s"%(res[-1], res[0], res[1]))
                res[1] = "私聊["+res[-1]+"]:" + res[1]
                for u in users:
                    if u["PORT"] == int(res[0]) and u["PORT"] != client.getpeername()[1]:
                        u["Client"].send(res[1].encode("gbk"))
                        break
                else:
                    client.send("该用户是自己或已下线".encode("gbk"))
            else:
                print("%s发送给所有人的消息:%s"%(res[-1], res[0]))
                res[0] = "all[" + res[-1] + "]:" + res[0]
                for u in users:
                    if u["PORT"] != client.getpeername()[1]:
                        u["Client"].send(res[0].encode("gbk"))

        else:
            # userlist.pop(str(cs.getpeername()[1]))
            # print("剩余客户端", len(userlist))
            # break
            users.remove(user)
            print("该用户已下线")
            break


def listen(server, users):
    while True:
        client, addr = server.accept()
        user = {"IP": addr[0], "PORT": addr[1], "Client": client}
        users.append(user)
        print("%s已连接,当前在线人数%d"%(addr[1], len(users)))
        t11 = Thread(target=get_and_send, args=(client, users, user))
        t11.start()


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('192.168.12.155', 6666))
    server.listen()
    users = []
    t1 = Thread(target=listen, args=(server, users))
    t1.start()
    t1.join()
