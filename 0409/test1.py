from multiprocessing import Pool
import os
import time


def fun(name, age, **kwargs):
    print("pid %d" % os.getpid())
    print(name, age, kwargs)
    time.sleep(1)


def main():
    pool = Pool(5)
    for i in range(20):
        pool.apply_async(fun, ("zzy", 20), {"isalive": False})
    pool.close()
    pool.join()
    print("finish")


if __name__ == '__main__':
    main()
