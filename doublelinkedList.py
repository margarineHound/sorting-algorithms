class DoubleLinkedSentinel(object):
    '''
    WORK IN PROGRESS - NOT YET COMPLETE
    Double Linked List implemented as a queue
    '''
    class Node(object):
        __slots__ = '_element', '_next', '_prev'
        def __init__(self, e = None, n = None, p = None):
            self._element = e
            self._next = n
            self._prev = p

    def __init__(self):
        self._head = None
        self._next = None
        self._tail = None
        self._prev = None
        self._size = None

    def getsize(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def tail(self):
        if self.getsize() == 0:
            print("List is empty")
            return
        else:
            return self._tail

    def top(self):
        if self.getsize() == 0:
            print("List is empty")
            return

        else:
            return self._head

    def last(self, n):
        self._prev = self.Node(n, None, self.last)
        self._tail = self._last

        if self.getsize() == 0:
            self._head = self._last

        self._size += 1


    def insert(self, e, pos, none):
        pass
    def push(self, e):
        self._head = self.Node(e, self._head)
        self._prev = None
        self._size += 1

        if self.__len__() == 0:
            self._last = self._head

    def get_next(self, n):
        return n._next

    def get_element(self, n):
        if self.is_empty:
            print("List is empty")
            return

        else:
            return n._element

    def __len__(self):
        return self._size
