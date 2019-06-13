"""
编写代码测试类属性实例属性 ，类方法静态方法实例方法，分析区别以及调用逻辑
"""


class Teacher():
    """
        first demo
    """
    is_ok = True

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def getname(self):
        print(self.name)
    # 类方法
    @classmethod
    def cmethod(cls):
        print(cls.__doc__)

    # 静态方法
    @staticmethod
    def smethod():
        print("static method")


# 对象实例化
t1 = Teacher("hcy", 20)
# 类属性
print(Teacher.is_ok)
# 实例属性
print(t1.name)
# 实例方法
# t1.getname()
# t1.smethod()
# t1.cmethod()


# 区别
# 实例方法用来操作实例属性
# 类方法可以访问到类的内容
# 静态方法不可访问类内容和实例内容

# 调用逻辑
# 实例方法必须实例化对象才能调用
# 类方法和静态方法 实例化对象和类都能调用
