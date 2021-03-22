from linked_list import Node

'''
Question: Define a function that takes a head node and an integer value n

The function should return the value of nth node to the tail

思路：召唤一个长度为n的模块，将其置于列表中，模块需要定义两个参数，即最左端和最右端，这两端都为node

之后，部署一个while loop，使模块在链表中逐步前进

当最右端的node指向None时，模块停止前进，while loop 终止

输出最左端的node的value
'''

def nth_to_end(n: int, head: Node):
    left_end = head
    right_end = head  # 模块初始化
    for i in range(n-1):

        if not right_end.next_node:
            raise LookupError('n is too large')

        right_end = right_end.next_node    # 模块设置完成

    while right_end.next_node:
        right_end = right_end.next_node
        left_end = left_end.next_node

    return left_end.value

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

assert nth_to_end(1,a) == 5
assert nth_to_end(2,a) == 4
assert nth_to_end(3,a) == 3
assert nth_to_end(4,a) == 2
assert nth_to_end(5,a) == 1

print('All tests are passed')