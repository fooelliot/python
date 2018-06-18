# 切片的语法[起始：结束：步长]
str = "hello world tom jack world"
# 字符串操作
print(str[2:-1])
print(str[2:])
print(str[:4])
print(str[::2])
print(str[0:4:2])
print(str[::-1])

#查找字符串第一次出现的索引 否则返回-1
print(str.find("jack"))
print(str.index("jack", 0, len(str)))
print(str.count("world"))
print(str.replace("world","world2"))

print(str.split(" ", 2))

nameList = ['tom', "jack", 123, "test", "andy"]
nameb = ['java', "python", "scala", "js"]
# for name in nameList:
#     print(name)
#
# i = 0
# while i < len(nameList):
#     print(nameList[i])
#     i += 1
# name = input("请输入添加的姓名")
# nameList.append(name)
# nameList.extend(nameb)
# nameList.insert(1, "demos")
# nameList[1] = "jammm"
# print(nameList)
# testName = input("请输入：")
# if testName not in nameList:
#     print(testName)
# else:
#     print("没有找到！")
# nameList.reverse("tom")
# print(nameList.pop())
# del nameList[1]
# nameList.sort(reverse=True)

ageList = (12,23,43)
print(ageList[1])
info = {'name':"zhangsan","age":12,"address":"guangdong"}
print(info)
print(info.get("names", "james"))
info["name"] = "lisi"
print(info)
info["bir"] = "2020"
print(info)


# del info["name"]
# del info
print("===")
print(info)
print(info.keys())
print(info.values())
print(len(info))
print(info.items())
print()
max(1,3)

