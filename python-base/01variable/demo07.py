def aa(a,b):
    shang = a//b
    yushu = a%b
    return shang, yushu


print(aa(5,2))
sh,yu = aa(5,2)
print(sh,yu)
def bb(a,b=23):
    print(a,b)

bb(5)

def cc(a,b,*args):
    print(a,b,args)

cc(12,23,45,34)

def dd(a,b,*args,**wcargs):
    print(a,b,args,wcargs)


dd(12,23,23,34,12,name="james",age=12,addres="guangzhou")
def calNum(num):
    if num >=1:
        result = num * calNum(num-1)
    else:
        result = 1
    return result

print(calNum(4))

sum = lambda a,b:a+b
print(sum(12,34))


def fun(a,b,opt):
    print("a=%d"%a)
    print("b=%d"%b)
    print("result=",opt(a,b))

fun(12,12,lambda x,y:x+y)

stus = [{"name":"zhangsan", "age":18}, {"name":"lisi", "age":19},{"name":"wangwu", "age":17} ]
stus.sort(key=lambda x:x['name'])
print(stus)

stus.sort(key=lambda x:x['age'])
print(stus)




