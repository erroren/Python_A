import threading
num = 0
def func():
    global num
    for i in range(10000):
        mutex.acquire()
        num += 1
        mutex.release()


def main():
    t1 = threading.Thread(target=func)
    t1.start()
    t2 = threading.Thread(target=func)
    t2.start()

    t1.join()
    t2.join()
    print(num)


if __name__ == '__main__':
    mutex = threading.Lock()
    main()















