def renameattr(classname, parentclass, attr):
    print(attr)
    newattr = {}
    for k, v in attr.items():
        if not k.startswith("__"):
            k = classname.lower()[0] + "_" + k
            newattr[k] = v
    return type(classname, parentclass, newattr)


class Student(object, metaclass=renameattr):
    id = None
    name = None
    age = None


S = Student()
print(S, type(S))
# print(S.__dir__())
print(Student.__dict__)

