def fib(times):
    a, b = 0, 1
    yield a
    yield b
    count = 0
    while count < times:
        a, b = b, a+b
        yield b
        count += 1
    return "aaa"


f = fib(5)
for i in f:
    print(i)
