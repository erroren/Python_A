from multiprocessing import Queue

if __name__ == '__main__':
    q1 = Queue(2)
    q1.put("aaa")
    q1.put("bbb")
    try:
        q1.put_nowait("ccc")
    except:
        print("put error")
    print("队列长度%d"%q1.qsize())
    res = q1.get()
    print(res)
    print("队列长度%d" % q1.qsize())
    res = q1.get_nowait()
    print(res)
    print("队列长度%d" % q1.qsize())
    try:
        res = q1.get_nowait()
        print(res)
    except:
        print("get error")

