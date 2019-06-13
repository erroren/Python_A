from multiprocessing import Pool
from multiprocessing import Manager
import time


def read(q):
    while True:
        print("正在读取数据。。。。队列长度:%d"% q.qsize())
        res = q.get()
        print("读取数据%d。。。。队列长度%d" % (res, q.qsize()))
        time.sleep(1)


def write(q):
    for i in range(20):
        print("正在写入。。。。队列长度:%d"% q.qsize())
        q.put(i)
        print("写入完成。。。。队列长度%d" % q.qsize())
        time.sleep(0.5)


if __name__ == '__main__':
    q = Manager().Queue(20)
    pool = Pool(5)
    pool.apply_async(write, (q,))
    pool.apply_async(read, (q,))
    pool.close()
    pool.join()
    print("finish")

