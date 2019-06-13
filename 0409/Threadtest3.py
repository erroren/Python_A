import threading
import time
num = 0


def fun1():
    global num
    for r in range(10000):
        mutex.acquire()
        num += 1
        mutex.release()


class MyThread(threading.Thread):
    def run(self):
        for r in range(10000):
            global num
            mutex.acquire()
            num += 1
            mutex.release()


def main():
    t1 = threading.Thread(target=fun1)
    t1.start()
    time.sleep(2)
    print("1", num)
    t2 = MyThread()
    t2.start()
    # t1.join()
    # t2.join()
    time.sleep(2)
    print("2", num)


if __name__ == '__main__':
    mutex = threading.Lock()
    main()
