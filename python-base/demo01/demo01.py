a = "lao"
b = "wang"
c = "zhao"

d = a + b

d
print(d)

print("==%s=="%(a+b))
name = "hello"
print(name[1])
print(len(name))
print(name[-1])
print("--------------")

e = "abcdeABCDE"
print(e[2:4])
print(e[2:-2])
print(e[2:])
print(e[2:6:1])
print(e[2:6:2])
print(e[2:6:3])
print(e[2:6:4])
print(e[-1:0:-1])

names = ["aa","bb","cc"]
print(names)

names.append("ee")
print(names)
names.insert(2,"ff")
print(names)
# names.clear()
print(names)
names.pop()
print(names)


if "aa" in names:
    print("找到了")
