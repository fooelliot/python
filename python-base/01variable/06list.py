# coding:utf-8

"""
    python 数组操作

"""

names = ["apple", "origin", "windows", "git", "linux", "max", "idea"]
other_list = ["andy", "james", "kobe", "lyon"]

# 输出完整列表
print(names)
# 输出列表第一个元素
print(names[0])
# 输出列表第二个至第三个元素
print(names[1:3])
# 输出列表第三个开始至末尾的所有元素
print(names[2:])
# 输出列表两次
print(names * 2)
# 输出拼接列表
print(names + other_list)

print("-------添加元素---------")
# 通过append可以向列表添加元素
names.append("ee")
print(names)

# insert(index, object) 在指定位置index前插入元素object
names.insert(2, "ff")
print(names)

# 通过extend可以将另一个集合中的元素逐一添加到列表中
names.extend(other_list)
print(names)

print("-------修改元素---------")
names[0] = "hello"
print(names)

print("-------查找元素---------")
# python中查找的常用方法为：
# in（存在）,如果存在那么结果为true，否则为false
# not in（不存在），如果不存在那么结果为true，否则false

if "ee" in names:
    print("找到了:%s" % "ee")

if "dd" not in names:
    print("没有找到:%s" % "dd")

# index和count与字符串中的用法相同
print(names.index("ee", 1, len(names)))

print(names.count("ee"))

print("-------删除元素---------")
# 列表元素的常用删除方法有：
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除

movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print('------删除之前------')
print(movieName)

# del movieName[2]
# movieName.pop()
movieName.remove('指环王')

print(movieName)
print('------删除之后------')

print('------排序(sort, reverse)------')

a = [1, 4, 2, 3]
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 列表嵌套

schoolNames = [['北京大学', '清华大学'],
               ['南开大学', '天津大学', '天津师范大学'],
               ['山东大学', '中国海洋大学']]
