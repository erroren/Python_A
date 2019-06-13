# 进程封装类
from multiprocessing import Process
import time


class Myprocess(Process):
    def run(self):
        while True:
            print("hi")
            time.sleep(1)


if __name__ == '__main__':
    p1 = Myprocess()
    p1.start()
