from  multiprocessing import Process
import  os


def process1():
    print("第一个进程")


def process2():
    print("第二个进程")


def main():
    p1 = Process(name="first", target=process1)
    p1.start()
    print(p1.pid)
    print(p1.name)
    print(p1.is_alive())
    p1.terminate()
    p1.join()
    print(p1.is_alive())
    p2 = Process(target=process2)
    p2.start()


if __name__ == "__main__":
    main()