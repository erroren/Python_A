from multiprocessing import Queue
from multiprocessing import Process
q = Queue(10)

def read(q):
    while True:
        print(q.qsize())
        res = q.get()
        print(res)
        print(q.qsize())


def write(q):
    for i in range(10):
        q.put(i)


def main():
    p2 = Process(target=write, args=(q,))
    p1 = Process(target=read, args=(q,))
    p2.start()
    p1.start()

    p2.join()
    p1.join()


if __name__  == "__main__":
    main()