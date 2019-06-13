import threading


num = 1


def func1():
    num = 2
    print(num)


func1()
print(num)


def func2():
    global num
    num = 3
    print(num)


func2()
print(num)

def func3():
    global num
    num = 4
    print(num)


t = threading.Thread(target=func3)
t.start()
print(num)

