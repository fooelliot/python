str = "hello world hello"

num = 1000
def demo1(a,b=23):
    global num
    print("hello funciton%d"%(a+b))
    print("修改之前%d"%num)

    num = 20
    print("修改之后%d"%num)
    return 1

print(demo1(2,3))

def demo2(a, b, *args, **kwargs):
    print("a=",a)
    print("b=",b)
    print("args=",args)
    print("kwargs=",kwargs)
demo2(1,2,3,4,5,m=4,n=5)

sum = lambda arg1, arg2:arg1+arg2

print(sum(12,34))
print(sum(34,89))
def fun (a,b,opt):
    print("a=",a)
    print("b=",b)
    print("result=",opt(a,b))

print(fun(1,2,lambda a,b:a+b))





