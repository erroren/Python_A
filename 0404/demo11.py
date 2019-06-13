import copy
# 浅拷贝  深拷贝
list1 = [1, 2, [5, 6]]
list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)

list2[1] = 3
print(list1, list2)
list3[0] = 2
print(list1, list3)
list4[0] = 5
print(list1, list4)
