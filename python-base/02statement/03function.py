
# coding:utf-8

"""
python 函数
def 函数名():
    代码

定义了函数之后，就相当于有了一个具有某些功能的代码，想要让这些代码能够执行，需要调用它
调用函数很简单的，通过 函数名() 即可完成调用
定义时小括号中的参数，用来接收参数用的，称为 “形参”
调用时小括号中的参数，用来传递给函数用的，称为 “实参”
想要在函数中把结果返回给调用者，需要在函数中使用return


局部变量，就是在函数内部定义的变量
不同的函数，可以定义相同的名字的局部变量，但是各用个的不会产生影响
局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储，这就是它的作用

如果一个变量，既能在一个函数中使用，也能在其他的函数中使用，这样的变量就是全局变量

"""


# 定义一个函数，能够完成打印信息的功能
def print_info():
    print('------------------------------------')
    print('人生苦短，我用Python')
    print('------------------------------------')


# 定义完函数后，函数是不会自动执行的，需要调用它才可以
print_info()


# help(print_info())

def number_sum(a, b):
    return a + b


print(number_sum(12, 23))


def number_max(a, b):
    if a > b:
        print("%d" % a)
    else:
        print("%d" % b)


number_max(12, 23)


# 一个函数里面又调用了另外一个函数，这就是所谓的函数嵌套调用
def test_b():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')


def test_a():
    print('---- testA start----')
    test_b()
    print('---- testA end----')


test_a()

c = 100

"""
    在函数外边定义的变量叫做全局变量
    全局变量能够在所有的函数中进行访问
    如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
    如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇
    
    在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
    对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
    对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。
    
    
    
    
"""


def test_c():
    # c = 200
    global c
    print("修改之前:%d" % c)
    c = 300
    print("修改之后:%d" % c)


test_c()


def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


print(divid(12, 4))


# 注意：带有默认值的参数一定要位于参数列表的最后面。
def test_d(name, age=35):
    # 打印任何传入的字符串
    print("Name: ", name)
    print("Age ", age)


print(test_d("james"))
print(test_d("kobe", 34))


# 不定长参数
# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
def fun(a, b, *args, **kwargs):
    """可变参数演示示例"""
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs: ")
    for key, value in kwargs.items():
        print(key, "=", value)


fun(1, 2, 3, 4, 5, m=6, n=7, p=8)  # 注意传递的参数对应

c = (3, 4, 5)
d = {"m": 6, "n": 7, "p": 8}

fun(1, 2, *c, **d)  # 注意元组与字典的传参方式

"""
匿名函数
用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。

lambda函数的语法只包含一个语句，如下：
"""

sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("Value of total : ", sum(10, 20))

print("Value of total : ", sum(20, 20))


def fun(a, b, opt):
    print("a =", a)
    print("b =", b)
    print("result =", opt(a, b))


fun(1, 2, lambda x, y: x + y)


stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]

stus.sort(key=lambda x: x['name'])
print(stus)
