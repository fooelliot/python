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

"""


a = 1;
b = 2;
c = 3.1;
d = 23.3;
e = True;
f = False;
g = "";
h = ["","",""];
name = "james hello james kobe";
print("hello%s"%name);
print(len(name))
print(name[1:3])
print(name[1:])
print(name[1:-1])

print(name.find('aa',0,len(name)))
print(name.index('a',0,len(name)))
print(name.count('james',0,len(name)))
print(name.replace('james','JAMES',1))

print(name.split(" "))
print(name.split(" ",2))

print(name.capitalize())
print(name.title())
print(name.startswith("ja"))
print(name.endswith("b"))

print(name.lower())
print(name.upper())

print(name.ljust(30))
print(name.rjust(30))
print(name.center(50))
print(name.rfind('d'))
print(name.rindex('o'))
print(name.isalpha())
print(name.join("0"))

nameList = ['aaa','bbb','ccc']
print(nameList[1])

for n in nameList:
    print(n)

print('---------------')
nameList.append("ddd")
print(len(nameList))
if 'ddd' in nameList:
    print(True)

if 'ddd' not in nameList:
    print(False)
else:
    print(True)

nameList.append('aaa')
print(nameList)
print(nameList.index('aaa'))
print(nameList.count('aaa'))

del nameList[0]
print(nameList)
print(nameList.pop())
print(nameList)
print(nameList.remove('bbb'))
print(nameList)
print(nameList.reverse())
print(nameList.sort())
