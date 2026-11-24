# -----------------------------------------------------------------------------------------
# Stack
class Stack():
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def stack_len(self):
        return len(self._items)
    
    def pop(self):
        if self.is_empty():
            raise EmptyError
        else:
            return self._items.pop()

    def push(self, item):
        self._items.append(item)

    def __str__(self):
        return str(self._items)

# -----------------------------------------------------------------------------------------
# Queue
class Queue():
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def queue_len(self):
        return len(self._items)
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyError
        else:
            return self._items.pop(0)

    def enqueue(self, item):
        self._items.append(item)

    def __str__(self):
        return str(self._items)

# -----------------------------------------------------------------------------------------
# Error handling for popping/dequeueing from empty Stack/Queue 
# (You don't have to implement this)
class EmptyError(Exception):
    def __str__(self):
        return "You are trying to pop/dequeue from an empty Stack/Queue"
