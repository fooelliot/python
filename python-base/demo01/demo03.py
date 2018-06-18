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
