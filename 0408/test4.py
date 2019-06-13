from multiprocessing import Process
import os


def process1(parm1, **kwargs):
    print("传进来的", parm1)
    parm1.append(1)
    print("修改后的", parm1)
    print("关键字传参", kwargs["name"])


def main():
    list1 = [3]
    p1 = Process(target=process1, args=(list1,), kwargs={"name": "hcy"})
    p1.start()
    p1.join()
    print("检查", list1)


if __name__ == "__main__":
    main()
