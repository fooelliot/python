# coding:utf-8
"""
Python包含了以下内置函数
序号	方法	                描述
1	cmp(item1, item2)	比较两个值
2	len(item)	        计算容器中元素个数
3	max(item)	        返回容器中元素最大值
4	min(item)	        返回容器中元素最小值
5	del(item)	        删除变量




"""
# print(cmp("hello", "itcast"))
# print(cmp("itcast", "hello"))
# print(cmp("itcast", "itcast"))
# print(cmp([1, 2], [3, 4]))
# print(cmp([1, 2], [1, 1]))
# print(cmp([1, 2], [1, 2, 3]))
# print(cmp({"a":1}, {"b":1}))
# print(cmp({"a":2}, {"a":1}))
# print(cmp({"a":2}, {"a":2, "b":1}))


print(len([1, 2, 3, 4]))
print(len((3, 4)))
print(len({"a": 1, "b": 2}))
print(len("hello world   print("))

print(max("hello world"))
print(max([1, 4, 522, 3, 4]))
print(max({"a": 1, "b": 2}))
print(max({"a": 10, "b": 2}))
print(max({"c": 10, "b": 2}))
