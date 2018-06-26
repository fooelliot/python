# coding:utf-8

def test(number):
    print("---1----")

    def test_in(number2):
        print("------2-----")
        print(number + number2)

    print("---3----")
    return test_in


b = test(200)

b(20)
b(30)
b(50)


def ww1(args):
    print(args)

    def w1(func):
        def inner(*args, **kwargs):
            print('w1 函数正在执行')
            return func(*args, **kwargs)

        return inner

    return w1


def f1(a, b, c):
    print("=====f1=====")
    return "hello"


@ww1("hellooooo")
def f2():
    print("=====f2=====")


# innerFunc = w1(f1)
# innerFunc()

f1 = w1(f1)
ret = f1(1, 2, 3)
print(ret)

f2()
