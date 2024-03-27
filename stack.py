class Stack:
    """ An implementation of stacks through a list and list methods. """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ Returns True or False depending on whether the stack is empty. """
        return not self.items

    def push(self, item):
        """ Add an item to the top of the stack. """
        self.items.append(item)

    def pop(self):
        """ Pop an item from the top of the stack.
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """ Returns the top element of the stack without popping it. """
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        """ Returns the number of items in the stack. """
        return len(self.items)
