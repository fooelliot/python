
class Car(object):
    def __init__(self,name,age):
        print('init 执行了')
        self.name = "andy"
        self.age = 12
        self.name = name
        self.age = age
    def __str__ (self):
        return "我叫%s"%self.name+"今年%d"%self.age
    def __del__(self):
        print("对象的销毁方法")


class Benchi(Car):
    def __init__(self,newName):
        self.name = newName
    pass

baoma = Car("james",32)
print(baoma.name)
print(baoma.age)
print(baoma)

benci = Benchi("benci",23)
print(benci.name)
print(benci.age)

try :
    print(nun)
    print("---")
except NameError :
    print("变量不存在！")
except FileNotFoundError:
    print("文件不存在异常")

try :
    open("xx.txt")
    print("---")
except (NameError, FileNotFoundError) :
    print("文件打开异常！")
except Exception:
    print("所有的异常父类")
finally:
    print("final里面的代码！")




def aa(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


print(aa(5, 2))
sh, yu = aa(5, 2)
print(sh, yu)


def bb(a, b=23):
    print(a, b)


bb(5)


def cc(a, b, *args):
    print(a, b, args)


cc(12, 23, 45, 34)


def dd(a, b, *args, **wcargs):
    print(a, b, args, wcargs)


dd(12, 23, 23, 34, 12, name="james", age=12, addres="guangzhou")


def calNum(num):
    if num >= 1:
        result = num * calNum(num - 1)
    else:
        result = 1
    return result


print(calNum(4))

sum = lambda a, b: a + b
print(sum(12, 34))


def fun(a, b, opt):
    print("a=%d" % a)
    print("b=%d" % b)
    print("result=", opt(a, b))


fun(12, 12, lambda x, y: x + y)

stus = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]
stus.sort(key=lambda x: x['name'])
print(stus)

stus.sort(key=lambda x: x['age'])
print(stus)
