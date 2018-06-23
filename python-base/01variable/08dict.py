# coding:utf-8

"""
    python 字典操作


"""

info = {'name': 'james', 'id': 100, 'sex': 'f', 'address': '美国 纽约'}
print(info['name'])
print(info['address'])

# 若info中不存在'age'这个键，就返回默认值18
print(info.get('age', 18))

# 修改元素
# new_id = input("please input new id:")
# info['id'] = int(new_id)
# print("修改之后的id为:%s" % info["id"])

# 添加元素
info["age"] = 12
print(info)

# 删除元素
# 对字典进行删除操作，有一下几种：del  clear()
print('删除前,%s' % info['name'])
del info['name']
# del info
print('删除后,%s' % info)

# 清空整个字典
print('清空前,%s' % info)

# info.clear()

print('清空后,%s' % info)

# 字典的常见操作2
print(len(info))
print(info.keys())
print(info.values())
print(info.items())

# 字典的遍历
for key in info.keys():
    print(key)

for value in info.values():
    print(value)

for item in info.items():
    print(item)

for key, value in info.items():
    print("key:%s,value:%s" % (key, value))


chars = ['a', 'b', 'c', 'd']
for i, chr in enumerate(chars):
    print(i, chr)
