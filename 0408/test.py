name = input("请输入商品名:")
price = input("请输入价格:")
g1 = type("Good", (), {"name": name, "price": price})
print(g1.name)
