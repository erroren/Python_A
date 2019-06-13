def renameclass(classname, parentclass,attr):
    newattr = {}
    classname = "new" + classname
    for k, v in attr.items():
        if  not k.startswith("__"):
            k = k+"attr"
            newattr[k] = v

    return type(classname, parentclass, newattr)


class Test2(metaclass=renameclass):
     id = None
     name = None
     age =None


t = Test2()
print(Test2.__name__)
print(Test2.__dict__)