import copy
list1 = [1, 3, 4, [5, 6]]
"=赋值"
list2 = list1
"浅拷贝"
list3 = copy.copy(list1)
"深拷贝"
list4 = copy.deepcopy(list1)
print(list1, list2, list3, list4)
# =赋值
# 改变列表list2中的元素，list1也改变
# list2[0] = 2
# 浅拷贝
# 改变列表list3，list4中的元素,list1不改变
# list3[0] = 2
# list4[1] = 2
# 如果列表嵌套的列表发生改变，原列表也改变
# list3[3][0] = 7
# 深拷贝
# 生成一个单独的个体
# 无论list4改变任意值，list1不会改变
list4[2] = 0
list4[3][1] = 9
print(list1, list2, list3, list4)
# list3[0] = 2
