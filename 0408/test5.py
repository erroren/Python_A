from multiprocessing import Process


class process1(Process):
    def run(self):
        print("运行run函数")


def main():
    p1 = process1()
    p1.start()


if __name__ == "__main__":
    main()