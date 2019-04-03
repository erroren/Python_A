def aa(mg):
    def check():
        name = input("请输入用户名:")
        if name == "aaa":
            mg()
        else:
            print("没有权限")
    return check


@aa
def selectmessage():
    print("查询列表")

selectmessage()

# selectmessage = aa(selectmessage)
# selectmessage()
