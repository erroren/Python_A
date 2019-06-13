from multiprocessing import Process
import os
import time


def p1process(parm1, **kwargs):
    # while True:
    time.sleep(3)
    print(parm1[0], kwargs["name"])
    print("进程1%d" % os.getpid())


def p2process():
    while True:
        print("进程2%d" % os.getpid())


def main():
    list1 = [1]
    p1 = Process(target=p1process, args=(list1,), kwargs={"name": "hcy"})
    p1.start()
    p1.join()
    # time.sleep(1)
    # p1.terminate()
    print("-------------")
    p2 = Process(target=p2process)
    p2.start()
    p2.join()
    # time.sleep(1)
    # p2.terminate()
    print("++++++++")


if __name__ == "__main__":
    main()
