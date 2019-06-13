from sys import getrefcount
print(getrefcount("aaa"))
a = "aaa"
print(getrefcount("aaa"))
b = "aaa"
print(getrefcount("aaa"))


list1 = [1, 2, 3]
print(getrefcount(list1))
list2 = list1
print(getrefcount(list1))
del list2
print(getrefcount(list1))


c = [4, 5]
d = [6, 7]
print(getrefcount(c))
print(getrefcount(d))
c.append(d)
# print(getrefcount(c))
print(getrefcount(d))


print(getrefcount(7))