# -*- coding: utf-8 -*-

"""

# coding:utf-8
# -*- coding: utf-8 -*-
文件头支付编码建议用第二种
python基础学习使用python3作为学习版本
第一章主要学习python基础之变量

"""

# hello world
print("hello world")

"""
    python 所有数据类型
    
        number(数字)
            int(有符号整型)
            long(长整型)
            float(浮点型)
            complex(复数)
            
        boolean(布尔)
            True
            False
            
        String(字符串)
        
        List(列表)
        
        Tuple(元组)
        
        Dictionary(字典)
        
        python 中使用type(name)查看数据类型
        python3已经不区分int和long
"""

"""
标示符由字母、下划线和数字组成，且数字不能开头建议单词之间用_连接，python区分大小写
python 中的关键字
and     as      assert     break     class      continue    def     del
elif    else    except     exec      finally    for         from    global
if      in      import     is        lambda     not         or      pass
print   raise   return     try       while      with        yield
"""


intNum = 100
longNum = 10000000000
floatNum = 1000000.0
complexNum = 1000000
string = "hello"

names = ["apple", "origin", "windows", "git", "linux"]

tuples = ("a", "b", "c", "d")

maps = {'name': 'john', 'code': 5762, 'age': 23}

print(type(intNum))
print(type(longNum))
print(type(floatNum))
print(type(complexNum))

print(type(string))
print(type(names))
print(type(tuples))
print(type(maps))


