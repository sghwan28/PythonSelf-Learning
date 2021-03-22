# Singly Linked List Implementation

# 优点1：对于数组来说，插入和删除的算法复杂度为O(n)。对于链表而言，需要的时间为常数K
# 优点2：链表可以持续扩张，无需再次声明数据结构的容量 参考 array.py 中 capacity 这个 attribute

# 缺点1：获取链表中第k个元素需要O(k)时间，对于数组而言，获取元素值的时间是O(1).
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next_node = b
# b.next_node = c
#
# assert a.next_node.value == 2


# Doubly Linked List Implementation
class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

# a = DoublyLinkedListNode(1)
# b = DoublyLinkedListNode(2)
# c = DoublyLinkedListNode(3)
#
# a.next_node = b
# b.prev_node = a
#
# b.next_node = c
# c.prev_node = b

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
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Stacks%2C%20Queues%20and%20Deques/Stacks%2C%20Queues%2C%20and%20Deques%20Interview%20Problems/Stacks%2C%20Queues%2C%20Deques%20Interview%20Questions%20-SOLUTIONS/Balanced%20Parentheses%20Check%20-%20SOLUTION.ipynb
'''

def balance_check(s):
    if len(s)%2 != 0:
        return False

    stack = []

    for i in s:
        if i in '{[(':
            stack.append(i)

    for i in s:
        if i in ']])':
            if len(stack) == 0:
                return False
            if i == ']':
                if stack.pop() != '[':
                    return False
            if i == ')':
                if stack.pop() != '(':
                    return False
            if i == '}':
                if stack.pop() != '{':
                    return False

    if len(stack) != 0:
        return False
    else:
        return True


print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))