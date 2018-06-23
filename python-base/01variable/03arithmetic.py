# coding:utf-8

"""
python运算符

    算术运算符
    下面以a=10 ,b=20为例进行计算
    运算符	描述	实例
    +	加	两个对象相加 a + b 输出结果 30
    -	减	得到负数或是一个数减去另一个数 a - b 输出结果 -10
    *	乘	两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
    /	除	x除以y b / a 输出结果 2
    //	取整除	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
    %	取余	返回除法的余数 b % a 输出结果 0
    **	幂	返回x的y次幂 a**b 为10的20次方， 输出结果 100000000000000000000

    赋值运算符
    运算符	描述	        实例
    =	    赋值运算符	把=号右边的结果给左边的变量 num=1+2*3 结果num的值为7

    复合赋值运算符
    运算符	描述	                实例
    +=	    加法赋值运算符	        c += a 等效于 c = c + a
    -=	    减法赋值运算符	        c -= a 等效于 c = c - a
    *=	    乘法赋值运算符	        c *= a 等效于 c =       c * a
    /=	    除法赋值运算符	        c /= a 等效于 c = c / a
    %=	    取模赋值运算符	        c %= a 等效于 c = c % a
    **=	    幂赋值运算符	        c **= a 等效于 c = c ** a
    //=	    取整除赋值运算符	    c //= a 等效于 c = c // a


    python中的比较运算符如下表
    运算符	描述	                                                示例
    ==	    检查两个操作数的值是否相等，如果是则条件变为真。	            如a=3,b=3则（a == b) 为 true.
    !=	    检查两个操作数的值是否相等，如果值不相等，则条件变为真。	    如a=1,b=3则(a != b) 为 true.
    <>	    检   查两个操作数的值是否相等，如果值不相等，则条件变为真。	    如a=1,b=3则(a <> b) 为 true。这个类似于 != 运算符
    >	    检查左操作数的值是否大于右操作数的值，如果是，则条件成立。	    如a=7,b=3则(a > b) 为 true.
    <	    检查左操作数的值是否小于右操作数的值，如果是，则条件成立。	    如a=7,b=3则(a < b) 为 false.
    >=	    检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3则(a >= b) 为 true.
    <=	    检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3则(a <= b) 为 true.


    逻辑运算符
    运算符	逻辑表达式	描述	                                                                实例
    and	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	    (a and b) 返回 20。
    or	    x or y	    布尔"或" - 如果 x 是 True，它返回 True，否则它返回 y 的计算值。	            (a or b) 返回 10。
    not	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	    not(a and b) 返回 False



    公共方法
    运算符	Python 表达式      	结果	                            描述	              支持的数据类型
    +	    [1, 2] + [3, 4]	    [1, 2, 3, 4]	                合并	              字符串、列表、元组
    *	    'Hi!' * 4	        ['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制	              字符串、列表、元组
    in	    3 in (1, 2, 3)	    True	                        元素是否存在	      字符串、列表、元组、字典
    not in	4 not in (1, 2, 3)	True	                        元素是否不存在	      字符串、列表、元组、字典

"""

a = 10
b = 20


print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

c, d = 2, 5
print(c,d)



# name = "james hello james kobe";
# print(len(name))
# print(name[1:3])
# print(name[1:])
# print(name[1:-1])
#
# print(name.find('aa',0,len(name)))
# print(name.index('a',0,len(name)))
# print(name.count('james',0,len(name)))
# print(name.replace('james','JAMES',1))
#
# print(name.split(" "))
# print(name.split(" ",2))
#
# print(name.capitalize())
# print(name.title())
# print(name.startswith("ja"))
# print(name.endswith("b"))
#
# print(name.lower())
# print(name.upper())
#
# print(name.ljust(30))
# print(name.rjust(30))
# print(name.center(50))
# print(name.rfind('d'))
# print(name.rindex('o'))
# print(name.isalpha())
# print(name.join("0"))
#
# nameList = ['aaa','bbb','ccc']
# print(nameList[1])
#
# for n in nameList:
#     print(n)
#
# print('---------------')
# nameList.append("ddd")
# print(len(nameList))
# if 'ddd' in nameList:
#     print(True)
#
# if 'ddd' not in nameList:
#     print(False)
# else:
#     print(True)
#
# nameList.append('aaa')
# print(nameList)
# print(nameList.index('aaa'))
# print(nameList.count('aaa'))
#
# del nameList[0]
# print(nameList)
# print(nameList.pop())
# print(nameList)
# print(nameList.remove('bbb'))
# print(nameList)
# print(nameList.reverse())
# print(nameList.sort())
