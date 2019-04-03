import time


def timestamp(fun):
    def func():
        begin = time.time()
        fun()
        end = time.time()
        print(fun.__name__, end-begin)
    return func


@timestamp
def AAA():
    time.sleep(2)


@timestamp
def BBB():
    time.sleep(3)


AAA()
BBB()