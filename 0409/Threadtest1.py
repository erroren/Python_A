import threading
import time


def ref():
    print("Aaa")
    time.sleep(1)


def main():
    for i in range(5):
        t1 = threading.Thread(target=ref, name="Thread"+str(i))
        t1.start()
        print(threading.currentThread().name, threading.currentThread().ident)
        print(len(threading.enumerate()))


if __name__ == "__main__":
    main()
