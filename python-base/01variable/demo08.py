f = open('test.txt','r')
# f.write("hello world james")
# print(f.read(4))
# print(f.read())

print(f.readline())
print(f.readlines())

for temp in f.readlines():
    print(temp)





f.close()
