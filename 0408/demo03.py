

def fun(x):
    return x


l1 = [1, 3, 4, 5, 6]
res = filter(fun, l1)
for i in res:
    print(i)
