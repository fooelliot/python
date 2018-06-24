# 切片的语法[起始：结束：步长]
str = "hello world tom jack world"
# 字符串操作
print(str[2:-1])
print(str[2:])
print(str[:4])
print(str[::2])
print(str[0:4:2])
print(str[::-1])

#查找字符串第一次出现的索引 否则返回-1
print(str.find("jack"))
print(str.index("jack", 0, len(str)))
print(str.count("world"))
print(str.replace("world","world2"))

print(str.split(" ", 2))

nameList = ['tom', "jack", 123, "test", "andy"]
nameb = ['java', "python", "scala", "js"]
# for name in nameList:
#     print(name)
#
# i = 0
# while i < len(nameList):
#     print(nameList[i])
#     i += 1
# name = input("请输入添加的姓名")
# nameList.append(name)
# nameList.extend(nameb)
# nameList.insert(1, "demos")
# nameList[1] = "jammm"
# print(nameList)
# testName = input("请输入：")
# if testName not in nameList:
#     print(testName)
# else:
#     print("没有找到！")
# nameList.reverse("tom")
# print(nameList.pop())
# del nameList[1]
# nameList.sort(reverse=True)


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

