"""
    编写代码添加类属性，实例属性，类方法，静态方法，实例方法，分析区别以及调用逻辑
删除指定 属性
"""
import types


class Student():
    __slots__ = ("name", "addr", "age","getname")

    def __init__(self,name):
        self.name = name


# 实例化对象
s1 = Student("hcy")
# 添加类属性
Student.addr = "xuchang"
print(Student.addr)
print(s1.addr)
# 添加实例属性
s1.age = 20
print(s1.age)


# 添加实例方法
def getname(self):
    print(self.name)


s1.getname = types.MethodType(getname, s1)
s1.getname()


# 添加类方法
@classmethod
def addcmethod(cls):
    print("add classmethod")


Student.cm = addcmethod
Student.cm()


# 添加静态方法
@staticmethod
def addsmethod():
    print("add static method")


Student.sm = addsmethod
Student.sm()


# del Student.sm
# Student.sm()
delattr(Student, "sm")
# Student.sm()

# 区别:
# 类属性每个实例化对象都能调用
# 实例化属性只能当前实例调用
# 类方法,静态方法每个对象都能调用
# 实例方法只能当前实例调用

