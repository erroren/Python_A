# 给现有的业务逻辑添加权限验证功能


# 定义装饰器函数并传入函数参数
def verify(fun):

    def check():
        # 权限验证
        name = input("请输入用户名")
        if name == 'hcy':
            # 执行参数函数
            fun()
        else:
            print("没有权限操作")
    # 返回check方法的引用
    return check


# 注释装饰器
@verify
def message():
    print("信息列表")


message()


import time


# 实现统计时间消耗装饰器
def statistic(fun):
    def check():
        begin = time.time()
        fun()
        end = time.time()
        print("运行", fun.__name__, "函数的是时间是:", end-begin)
    return check


@statistic
def sleepfunc():
    time.sleep(2)


sleepfunc()
