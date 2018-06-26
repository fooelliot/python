# coding:utf-8

"""
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去

在python中方法名如果是__xxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

"""


class User(object):
    """
    定义一个user类
    """

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __getattr__(self, item):
        print(item)
        return self

    def __str__(self):
        msg = "这个类似java中的toString方法,属性有name:" + self.name + ",age:" + str(self.age) + ",sex:" + self.sex
        print(msg)
        return msg


user = User("james", 12, "男")
user.__str__()
