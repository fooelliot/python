stu_a = {        "name":"A",        "age":21,        "gender":1,        "hometown":"aaa" }
stu_b = {        "name":"B",        "age":22,        "gender":0,        "hometown":"bbb" }
stu_c = {        "name":"C",        "age":20,        "gender":1,        "hometown":"ccc" }
def stu_intro(stu):
    """函数说明"""
    for key, value in stu.items():
        print(key,value)
stu_intro(stu_a)

class Car:
    def getCarInfo(self):
        print("车轮个数：%d,颜色%s"%(self.wheelNum,self.color))
    def move(self):
        print("车正在跑")

    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

bmw = Car()
bmw.color='黑色'
bmw.wheelNum=4
bmw.move()
print(bmw.color)
print(bmw.wheelNum)


class Person:
    def __init__(self,wheel,color):
        self.wheel=wheel
        self.color=color
        print("init")
    def __str__(self):
        msg = "hi...我的颜色是"+self.color
        return msg
    def move(self):
        print("车在跑")


person = Person(3,'green');
print(person.color)
print(person.wheel)
person.move()
print(person.__str__())
print(id(person))

class Animal(object):
    def __init__(self,name):
        self.name = name
    def printName(self):
        print("name:%s"%self.name)

def myPrint(animal):
    animal.printName()

dog1 = Animal("tom")
myPrint(dog1)















