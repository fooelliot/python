# coding:utf-8

"""
    python 字符串操作
    双引号或者单引号中的数据，都是字符串
下标索引
所谓“下标”，就是编号，就好比客车的座位号

"""

name = 'kobe'
position = '篮球运动员'
address = '美国 加利福尼亚州 洛杉矶'

print('--------------------------------------------------')
print("姓名：%s" % name)
print("职位：%s" % position)
print("地址：%s" % address)
print('--------------------------------------------------')

# username = input('请输入用户名:')
# print("用户名为：%s" % username)
# password = input('请输入密码:')
# print("密码为：%s" % password)

string = '  abc deaf gh ai ja ak lmn  '
print(string[0])
print(string[1])
print(string[2])

print("输出完整字符串:" + string)
print("输出字符串中的第一个字符:" + string[0])
print("输出字符串中第三个至第五个之间的字符:" + string[2:5])
print("输出从第三个开始到最后的字符串:" + string[2:])
print("输出字符串两次:" + string * 2)
print("输出连接的字符串:" + 'say: ' + string)

print(string[1])
print(len(string))
print(string[-1])
print(string[2:4])
print(string[2:-2])
print(string[2:])
print(string[2:6:1])
print(string[2:6:2])
print(string[2:6:3])
print(string[2:6:4])
print(string[-1:0:-1])

print("--------------")

# 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
print(string.find("a"))
print(string.find("b", 0, len(string)))

# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
print(string.index("d", 0, len(string)))

# 返回 str在start和end之间 在 mystr里面出现的次数
print(string.count("a", 0, len(string)))

# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
print(string.replace("a", "z", string.count("a")))
print(string)

# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
print(string.split(" ", 2))

# 把字符串的第一个字符大写
print(string.capitalize())

# 把字符串的每个单词首字母大写
print(string.title())

# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
print(string.endswith("de"))

# 转换 mystr 中所有大写字符为小写
print(string.lower())

# 转换 mystr 中的小写字母为大写
print(string.upper())

# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print(string.ljust(36) + "end")

# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print("start" + string.rjust(36))

# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print("start" + string.center(48) + "end")

# 删除 mystr 左边的空白字符
print(string.lstrip())

# 删除 mystr 字符串末尾的空白字符
print(string.rstrip())

# 删除mystr字符串两端的空白字符
print(string.strip())

# 类似于 find()函数，不过是从右边开始查找.
print(string.rfind("aa", 0, len(string)))

# 类似于 index()，不过是从右边开始.
print(string.rindex("a", 0, len(string)))

#把mystr以str分割成三部分,str前，str和str后
print(string.partition(" "))

#类似于 partition()函数,不过是从右边开始.
print(string.rpartition("a"))

#按照行分隔，返回一个包含各行作为元素的列表
print(string.splitlines())

# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
print(string.isalpha())


# 如果 mystr 只包含数字则返回 True 否则返回 False.
print(string.isdigit() )


# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
print(string.isalnum())


# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
print(string.isspace())


# mystr 中每个字符后面插入str,构造出一个新的字符串
print(string.join(str))



