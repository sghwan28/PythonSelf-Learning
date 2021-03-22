# stack LIFO: Last in First out

class Stack(object):

    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def __len__(self):
        return len(self.items)

# Below are for test
a = Stack()
assert a.isempty() == True
a.push(1)
assert a.peek() == 1
a.push(2)
a.push(3)
a.push(4)
assert a.peek() == 4
assert a.pop() == 4
assert len(a) == 3

print('All tests passed')
