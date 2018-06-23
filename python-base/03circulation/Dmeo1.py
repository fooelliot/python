a = [11,22,33]


b = [11,22,33]
print(a == b)
print(a is b)
print(id(a))
print(id(b))
c = a
print(c is a)
print("----")
d = 12
e = d
print(d is e)
print(e == d)
import copy

aa = [12,33,11]
bb = aa
print(aa == bb)
print(aa is bb)
print(id(aa))
print(id(bb))
bb = copy.deepcopy(aa)
print(bb is aa)
print(id(aa))
print(id(bb))
print("--------")
cc = [a,b]

print(cc)
dd = copy.deepcopy(cc)
a.append(44)
print(cc[0])
print(dd[0])
print("----------")
class Person():
    def __init__(self):
        self.__num = 12
        self.__age = 23

    def setNum(self, num):
        print("setNum---")
        self.__num = num

    def getNum(self):
        print("getNum---")
        return self.__num

    num = property(getNum,setNum)


    @property
    def age(self):
        print("getAge---")
        return self.__age

    @age.setter
    def age(self, age):
        print("setAge---")
        self.__age = age




p = Person()
p.setNum(233)
print(p.getNum())
p.num = 230
print(p.getNum())
print(p.num)

p.age = 34
print(p.age)




nums = [12, 23, 14, 32]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print("------------------")
for num in nums:
    print(num)


f = open('test.txt','r')
# f.write("hello world james")
# print(f.read(4))
# print(f.read())

print(f.readline())
print(f.readlines())

for temp in f.readlines():
    print(temp)





f.close()



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
