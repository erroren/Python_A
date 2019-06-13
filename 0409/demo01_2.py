from threading import Thread
import time

# 线程封装类
class Mythread(Thread):
    def run(self):
        while True:
            print("hi")
            time.sleep(1)


if __name__ == '__main__':
    t1 = Mythread()
    t1.start()