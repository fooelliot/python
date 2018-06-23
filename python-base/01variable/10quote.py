# coding:utf-8

"""
在python中，值是靠引用来传递来的。
我们可以用id()来判断两个变量是否为同一个值的引用。 我们可以将id值理解为那块内存的地址标示。
"""

a = 1
b = a
print(id(a))
print(id(b))

a = 2

print(id(a))




















