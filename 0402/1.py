# 使用列表推导式构造生成器，使用next和for循环得到内容
list1 = (x for x in range(10))
# 使用for循环
for i in list1:
    print(i)
# 使用next
while True:
    try:
        print(next(list1))
    except StopIteration as e:
        print(e)
        break

# 使用yield得到函数式生成器，内部存储裴波拉契数列
def field(count):
    a, b = 0, 1
    yield a
    yield b
    index = 0
    while True:
        if index < count:
            a, b = b, a+b
            yield b
            index += 1
        else:
            return "aaa"


r = field(5)
# for i in r:
#     print(i)
# 使用next 遍历完后就得到return的返回内容
while True:
    try:
        print(next(r))
    except StopIteration as e:
        print(e)
        break

