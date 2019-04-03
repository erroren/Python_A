import types


class Teacher():
    """
    demo01
    """

    __slots__ = ('name', 'age', 'addr', 'move')
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        print(self.name)


    @property
    def sage(self):
        return self.age

    @sage.setter
    def sage(self, age):
        self.age = age


    @classmethod
    def printage(cls):
        print(cls.__doc__)

    @staticmethod
    def pprint():
        print("aaaa")


T1 = Teacher("hcy", 20)
# T1.getname()
# T1.printage()
# T1.pprint()
print(T1.sage)
T1.sage = 15
print(T1.sage)


def move(self):
    print("实例方法")


T1.move = types.MethodType(move, T1)

T1.move()


@classmethod
def move1(cls):
    print("classmethod", cls.__doc__)


Teacher.move1 = move1
T1.move1()


@staticmethod
def move2():
    print("static Method")


Teacher.move2 = move2
T1.move2()


