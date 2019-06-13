from multiprocessing import Pool
import os
import time


def func(num):
    # while True:
    time.sleep(1)
    print("pid %d parent %d  %d" % (os.getpid(), os.getppid(), num))


def main():
    print("pid %d parent %d" % (os.getpid(), os.getppid()))
    pool = Pool(4)
    for i in range(20):
        # pool.apply(func, (i,))
        pool.apply_async(func, (i,))
    # pool.apply_async(func)
    # pool.apply_async(func)
    # pool.apply_async(func)
    # pool.apply_async(func)
    # pool.apply(func)
    # pool.apply(func)
    # pool.apply(func)
    # pool.apply(func)
    pool.close()
    pool.join()
    # pool.terminate()
    # pool.join()
    print("finish")


if __name__ == "__main__":
    main()
