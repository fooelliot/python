# coding:utf-8

"""
python 的文件操作
在python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件
open(文件名，访问模式)
关闭文件
close( )

访问模式	    说明
r	        以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	        打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	        打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
rb	        以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
wb	        以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
ab	        以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
r+	        打开一个文件用于读写。文件指针将会放在文件的开头。
w+	        打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a+	        打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
rb+	        以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
wb+	        以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
ab+	        以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

"""

# 写数据(write)
# f = open('../hello.txt', 'w')
# f.write('hello world, i am here!\njames')
# f.close()

# 读数据(read)
# 如果open是打开一个文件，那么可以不用谢打开的模式，即只写 open('test.txt')
# 如果使用读了多次，那么后面读取的数据是从上次读完后的位置开始的

# f = open('../hello.txt', 'r')
# content = f.read(5)
# print(content)
# print("-" * 30)
# content = f.read()
# print(content)
# f.close()

# 读数据（readlines）
# 就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素#

# f = open('../hello.txt', 'r')
# content = f.readlines()
# print(type(content))
# i = 1
# for temp in content:
#     print("%d:%s" % (i, temp))
#     i += 1
#
# f.close()


# oldFileName = input("请输入要拷贝的文件名字:")
#
# oldFile = open(oldFileName, 'r')
#
# # 如果打开文件
# if oldFile:
#
#     # 提取文件的后缀
#     fileFlagNum = oldFileName.rfind('.')
#     if fileFlagNum > 0:
#         fileFlag = oldFileName[fileFlagNum:]
#
#     # 组织新的文件名字
#     newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
#
#     # 创建新文件
#     newFile = open(newFileName, 'w')
#
#     # 把旧文件中的数据，一行一行的进行复制到新文件中
#     for lineContent in oldFile.readlines():
#         newFile.write(lineContent)
#
#     # 关闭文件
#     oldFile.close()
#     newFile.close()


# file = open("../hello.txt", "r")
# content = file.readlines()
# print(type(content))
# for line in content:
#     print(line)

# old_file_name = input("请输入备份的文件名:")
# old_file = open(old_file_name, "r")
# print(old_file)
# if old_file:
#     file_flag_num = old_file_name.rfind(".")
#     if file_flag_num > 0:
#         file_flag = old_file_name[file_flag_num:]
#
#     new_file_name = old_file_name[:file_flag_num] + "[复制]" + file_flag
#     new_file = open(new_file_name, "w")
#     for line in old_file.readlines():
#         new_file.write(line)
#     old_file.close()
#     new_file.close()


