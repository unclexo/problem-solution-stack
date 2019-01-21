class ArrayStack:
    """ LIFO Stack implementation using python list as underlying storage """

    def __init__(self):
        """ Create an empty stack """
        self._data = []

    def __len__(self):
        """ Returns the number of elements in the stack """
        return len(self._data)

    def is_empty(self):
        """ Returns true if the stack is empty """
        return len(self._data) == 0

    def push(self, element):
        """ Adds an element to the top of the stack """
        self._data.append(element)

    def top(self):
        """ Returns (but does not remove) the top element of the stack

        Raises Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """ Returns and removes an element from the top of the stack

        Raises Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass
