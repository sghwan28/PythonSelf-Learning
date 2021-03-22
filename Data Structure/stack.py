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
print(' ')

# Interview Question
'''
Balanced Parentheses Check 
Opened bracket = Right bracket; Closed bracket = Left bracket 

共有三种括号，分别为(), [], {} 检查一串字符串，判断括号使用是否规范

注意([])是合法的    但([)]非法

思路：使用堆栈的方法解题，算法框架如下：
1. 用for loop 遍历字符串，如果是左括号就放入堆栈中
2. 再一次遍历字符串，出现右括号就pop一次堆栈，并检查是否匹配，如果有任何不匹配 return false
3. 如果检出右括号时，堆栈为空 return false
4. 遍历完成后，如果堆栈还有剩余， return false
5. 遍历结束，堆栈为空，return true

'''

def balance_check(s):
    if len(s)%2 != 0:
        return False
    opening = ['(','[','{']
    matches = [')',']','}']
    stack = []

    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if (stack.pop(),i) not in tuple(zip(opening,matches)):
                return False

    return len(stack) == 0

assert balance_check('[]') == True
assert balance_check('[](){([[[]]])}') == True
assert balance_check('()(){]}') == False
print('balance check passed')
