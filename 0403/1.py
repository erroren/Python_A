def getinfo(self):
    print("id", self.id)
    print("name", self.name)


Goods = type("Goods", (), {"id": 1, "name": "hcy", "getinfo": getinfo})


def getname(self):
    print(self.name)


Food = type("Food", (Goods, ), {"id": 2, "name": "zzz", "getname": getname})
g1 = Goods()
f1 = Food()
g1.getinfo()
f1.getinfo()
f1.getname()