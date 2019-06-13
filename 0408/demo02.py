import json
class Good():
    def __init__(self, name, price):
        self.name = name
        self.price = price


# name = input("请输入商品名:")
# price = input("请输入价格:")
# g1 = Good(name, price)
# with open("a.json", "w") as file1:
#     json.dump(g1.__dict__, file1)
with open("a.json", "r") as file2:
    res = json.load(file2)
    print(res)
    for i, j in res.items():
        print(i, j)
