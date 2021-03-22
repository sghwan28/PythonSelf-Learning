# queue FIFO: First in first out

class Queue(object):
    def __init__(self):
        self.items =[]

    def isempty(self):
        return self.items == []

    def enqueue(self,n):
        self.items.insert(0,n)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


# Interview Question
'''
Implement a Queue using two stacks

Do not use the define stack class, instead, using the python list as your stack 

'''

class Queue2stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,n):
        self.instack.append(n)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


q = Queue2stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())