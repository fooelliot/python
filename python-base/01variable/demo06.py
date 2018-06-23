

def add2sum(a,b):
    c = a + b
    print(c)

# print(add2sum(12,23))

def sum2(a,b):
    return a+b

print(sum2(23,34))

def a():
    print("hello")

aa = 200
def b():
    global  aa
    aa = 3
    print("start")
    a()
    print("end%d"%aa)

b()
