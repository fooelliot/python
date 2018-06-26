import copy


class Person():
    def __init__(self):
        self.__num = 12
        self.__age = 23

    def setNum(self, num):
        print("setNum---")
        self.__num = num

    def getNum(self):
        print("getNum---")
        return self.__num

    num = property(getNum, setNum)

    @property
    def age(self):
        print("getAge---")
        return self.__age

    @age.setter
    def age(self, age):
        print("setAge---")
        self.__age = age


p = Person()
p.setNum(233)
print(p.getNum())
p.num = 230
print(p.getNum())
print(p.num)

p.age = 34
print(p.age)

