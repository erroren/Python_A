def func1(a):
    def func2(b):
        nonlocal a
        a = a + b
        return a+b
    return func2


f = func1(10)
print(f(2))

