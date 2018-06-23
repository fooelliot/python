
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
