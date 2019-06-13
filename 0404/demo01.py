class Teacher():
    isAlive = False

    def __init__(self,name,age):
        self.name = name
        self.age = age


T1 = Teacher("hcy", 20)
print(T1.name, T1.age)
print(T1.isAlive)
T1.isAlive = True
print(T1.isAlive)

