class Stack(object):
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        if self.__items:
            return self.__items[-1]

    def size(self):
        return len(self.__items)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    print(s.size())
    print(s.is_empty())
    s.pop()
    s.pop()
    print(s.peek())
    print(s.size())
    print(s.is_empty())


