# coding:utf-8

"""
python的语句学习
if 要判断的条件:
        条件成立时，要做的事情
"""

a = 100

b = 200

print("------简单if判断------")

if a >= 100:
    print("条件成立")

print("------简单if判断------")
if a >= 10:
    print("条件成立走a分支")
else:
    print("条件成立走b分支")

print("------多重if判断------")
if a >= 1:
    print("条件成立走a分支")
elif a >= 2:
    print("条件成立走b分支")
else:
    print("条件成立走c分支")

print("------嵌套if判断------")
if b == 200:
    print("条件成立")
    if a < 100:
        print("内部条件成立")
    else:
        print("内部条件不成立")
else:
    print("条件不成立")


