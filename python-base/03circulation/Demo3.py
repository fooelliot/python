import time

import timeit

start_time = time.time()

# // time = 185
# for a in range(0 ,1001):
#     for b in range(0 ,1001):
#         for c in range(0 ,1001):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))
# end_time = time.time()
# print("time:%d"%(end_time-start_time))

# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print("a,b,c:%d,%d,%d"%(a,b,c))
# end_time = time.time()
# print("time:%d"%(end_time-start_time))


# li1 = [1, 2]
# li2 = [23, 5]
# li = li1 = li2
#
# li = [i for i in range(10000)]
# li = list(range(10000))

def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li += i

def test3():
    li = list(range(10000))

def test4():
    li = [i for i in range(10000)]


timer1 = Timer("test1()", "from __main__ import test1")
print(time1.timeit)
timer2 = Timer("test2()", "from __main__ import test2")
print(time2.timeit)
timer3 = Timer("test3()", "from __main__ import test3")
print(time3.timeit)
timer4 = Timer("test4()", "from __main__ import test4")
print(time4.timeit)










