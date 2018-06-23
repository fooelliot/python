

class Queue(object):

    def __init__(self):
        self.__List = []

    def enqueue(self, item):
        self.__List.append(item)

    def dequeue(self):
        self.__List.pop(0)


    def ie_empty(self):
        return self.__List == []

    def size(self):
        return len(self.__List)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
