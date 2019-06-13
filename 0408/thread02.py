from multiprocessing import Process

def p1process():
    print("自定义进程")


class mythread(Process):
    def __init__(self, target):
        Process.__init__(self, target=target)

    def run(self):
        print("运行Mythread")


def main():
    data = 1
    p1 = mythread(target=p1process)
    p1.start()


if __name__ == "__main__":
    main()
