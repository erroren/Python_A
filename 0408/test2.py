from multiprocessing import Process
import os


def processone():
    print("第一个进程%d，父进程%d"%(os.getpid(), os.getppid()))


def processtwo():
    print("第二个进程%d，父进程%d" % (os.getpid(), os.getppid()))

def main():
    p1 = Process(target=processone)
    p1.start()
    p2 = Process(target=processtwo)
    p2.start()


if __name__ == "__main__":
    main()