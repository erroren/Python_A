from multiprocessing import Queue

def main():
    q = Queue(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    res = q.get(1)
    print(res)
    print(q.empty())
    print(q.full())


if __name__ == "__main__":
    main()
