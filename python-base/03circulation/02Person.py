# coding:utf-8


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("this is init method")

    def __str__(self):
        print("this is str method")

    def __del__(self):
        print("this is delete method")

    def hello(self):
        print("hello")


person = Person("james", 12)


