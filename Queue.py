# 普通队列
class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)
        # self.__list.insert(0,item)

    def dequeue(self):
        return self.__list.pop(0)
        # return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


# 双端队列
class Deque(object):
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def po_front(self):
        return self.__list.pop(0)

    def po_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
