class Slinked(object):
    '''
    A Singly linked list implemented as a stack
    '''
    class _Node(object):

        __slots__ = '_element', '_next'

        def __init__(self, element, next_e):
            self._element = element
            self._next = next_e
            print("new element added")

    def __init__(self):
        ''' create an empty list'''
        self._head = None
        self._size = 0
        self._tail = None


    def push(self, e, pos=None):

        self._head = self._Node(e, self._head)
        if self._tail == None:
            self._tail = self._head
        self._size += 1

    def top(self):
        '''Return the first element in the Single Linked list'''
        if self.is_empty():
            print("List is empty")
            return

        else:
            return self._head._element

    def tail(self):
        return self._tail

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def get_next(self, n):
        return n._next


    def get_element(self, n):

        if self.is_empty():
            return
        else:
            return n._element

    def get_size(self):
        return self._size

    def __len__(self):
        return self._size

    def pop(self, n=1):

        if self.is_empty():
            return
        elif n> self.get_size():
            print("Index out of range. List size: ", self.get_size())
            return
        else:
            temp = []
            while (n > 0):
                temp.append(self.top())
                self._head = self._head._next
                self._size -= 1
                n -= 1
                if self._size == 0:
                    print("List is now Empty")
                    break

            return temp
    def __repr__(self):
        a = []
        current = self._head
        for i in range(self._size):
            a.append(self.get_element(current))
            a_next = self.get_next(current)
            if a_next:
                current = a_next
        return ','.join(a)

if __name__ == "__main__":
    a = Slinked()
    a.push('integer')
    a.push('help')
    a.push('me')
    # ina = a.get_element(1)
    repr(a)
    print(repr(a))
    ina = a.top()
    print(ina)
    a.pop()
    print(a.get_size())
    # repr(a)