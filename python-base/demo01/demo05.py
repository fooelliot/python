#字典
info = {'name':'james','age':'12','sex':'boy'}

print(info['name'])
print(info['age'])
print(info.get('sex'))
print(info)
# print(info.clear())
print(len(info))
print(info.keys())
print(info.values())
print(info.items())

for i in info:
    print(i)


for ii in info.keys():
    print(ii)

for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
print([1, 2] + [3, 4])
print("hello"*4)
print(2 in (1,2,3))
print(3 not in (2,3,4))

print(len("hello"))
print(max([2,23]))
print(min([2,23]))


