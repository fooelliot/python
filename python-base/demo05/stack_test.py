
class Stack(object):
    """栈的操作"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


if __name__ == "__name__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
