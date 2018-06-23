# coding:utf-8

"""
    python 元组操作
    Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号
    python中不允许修改元组的数据，包括不能删除其中的元素。
"""

aTuple = ('hello', 77, 99.9)
print(aTuple)

print(aTuple[0])
print(aTuple[1])
print(aTuple[2])


# 元组的内置函数count, index
# index和count与字符串和列表中的用法相同
a = ('a', 'b', 'c', 'a', 'b')
# 注意是左闭右开区间
# print(a.index('a', 1, 3))
print(a.index('a', 1, 4))
print(a.count('b'))
