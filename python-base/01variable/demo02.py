# coding:utf-8

"""
格式符号	转换
%c	字符
%s	通过str() 字符串转换来格式化
%i	有符号十进制整数
%d	有符号十进制整数
%u	无符号十进制整数
%o	八进制整数
%x	十六进制整数（小写字母）
%X	十六进制整数（大写字母）
%e	索引符号（小写'e'）
%E	索引符号（大写“E”）
%f	浮点实数
%g	％f和％e 的简写
%G	％f和％E的简写
"""

string = "hello"
print("python的输出string:%s,number%d" % (string, 12))
# 会在一行显示
print("1234567890====")
# 一行显示1234567890，另外一行显示====
print("1234567890\n====")

"""
python3版本中
没有raw_input()函数，只有input()
并且python3中的input与python2中的raw_input()功能一样
的小括号中放入的是，提示信息，用来在获取数据之前给用户的一个简单提示
在从键盘获取了数据以后，会存放到等号右边的变量中
会把用户输入的任何值都作为字符串来对待
"""

name = input("please input you name:")
age = input("please input you age:")

print(age)
print(type(name))
print(name)
print(type(name))

