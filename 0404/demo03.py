L = [x for x in range(10)]
print(L, type(L), L.__sizeof__())
L1 = (x for x in range(10))
print(L1, type(L1), L1.__sizeof__())
# print(L1.__next__())


def run(L1):
    for i in L1:
        yield i


r = run(L1)
while True:
    try:
        print(next(r))
    except Exception as e:
        print(e)
        break
