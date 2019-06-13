from threading import Thread
import time


def prt():
    print("aaaaa")
    time.sleep(1)


def timecount(ms):
    def func():
        begin = time.time()
        ms()
        end = time.time()
        print(ms.__name__, end-begin)
    return func


@timecount
def main():
    listThread = []
    for i in range(5):
        t1 = Thread(target=prt)
        t1.start()
        listThread.append(t1)

    for i in listThread:
        i.join()


if __name__ == "__main__":
    main()
