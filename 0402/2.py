from collections.abc import Iterable, Iterator
list1 = ["list1", "list2", "list3"]
tuple1 = (2, 3, 54)
dict1 = {"name": "hcy", "age": 18}
str1 = "aaa"
i = 100
print("列表是否可迭代", isinstance(list1, Iterable))
print("列表是否是迭代器", isinstance(list1, Iterator))
print("元组是否可迭代", isinstance(tuple1, Iterable))
print("元组是否是迭代器", isinstance(tuple1, Iterator))
print("字典是否可迭代", isinstance(dict1, Iterable))
print("字典是否是迭代器", isinstance(dict1, Iterator))
print("字符串是否可迭代", isinstance(str1, Iterable))
print("字符串是否是迭代器", isinstance(str1, Iterator))
print("整数是否可迭代", isinstance(i, Iterable))
print("整数是否是迭代器", isinstance(i, Iterator))
