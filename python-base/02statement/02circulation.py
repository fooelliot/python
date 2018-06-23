# coding:utf-8

"""
python 循环语句

"""

i = 0
while i < 10:
    print("while循环,这是第%d次循环" % i)
    i += 1

x = 1
sum = 0

while x <= 100:
    sum += x
    x += 1
print("1~100的累积和为:%d" % sum)

y = 1
result = 0
while y <= 100:
    if y % 2 == 0:
        result += y
    y += 1
print("1~100的累积和为:%d" % result)

a = 1
while a <= 5:
    j = 1
    while j <= a:
        print("*", end='')
        j += 1
    print("\n")
    a += 1

b = 1
while b <= 9:
    c = 1
    while c <= b:
        print("%d*%d=%-2d " % (c, b, b * c), end='')
        c += 1
    print("\n")
    b += 1

print("----for循环----")

name = 'hello world'

for e in name:
    print(e)

name = ''
for d in name:
    print(d)
else:
    print("没有数据")

print("----break----")
for f in 'hello world':
    if f == ' ':
        break
    print(f)

print("----continue----")
for g in 'hello world':
    if g == ' ':
        continue
    print(g)


h = 0
while h < 10:
    h = h + 1
    print('----')
    if h == 5:
        break
    print(h)

r = 0
while r < 10:
    r = r + 1
    print('----')
    if r == 5:
        continue
    print(r)


