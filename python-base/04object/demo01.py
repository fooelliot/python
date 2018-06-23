# import sys
# class Dog:
#     def set_age(self,new_age):
#         if new_age < 100 and new_age > 0:
#             self.age = new_age
#         else:
#             self.age=1
#     def __init__(self):
#         print("----init------")
#
#     def get_age(self):
#         return self.age
#
#
#     def test1(self):
#         print("----test1----------")
#         self.__test2()
#     def __test2(self):
#         print("-----test2---------")
#
#     def __del__(self):
#         print("对象的del方法！")
#
#     def my(self):
#         print("dog my method")
# dog = Dog()
# dog.set_age(102)
#
# age = dog.get_age()
# print(age)
#
# dog.test1()
# dog.__init__()
# print(sys.getrefcount(dog))
# del dog
#
# class T:
#     pass
# t=T()
# tt = t
# # del tt
#
# class D(Dog):
#     num = 0
#     def my(self):
#         print("this my method")
#         Dog.my(self)
#         super().my()
#
#     @classmethod
#     def the(cls):
#         cls.num = 12
#         print("hello")
#     @staticmethod
#     def abc():
#         print("static method")
#     pass
#
# ddd = D()
# ddd.test1()
# ddd.my()
# D.the()
#
# print(D.__mro__)
#
# test.test
