'''

Question 1 : define a function to check if a linked list circular
The function should return a boolean value, True or False

思路：假设该链表为一条赛道，在该赛道上的相同位置召唤两个工具人分别为 maker1 和 maker2，之后设置一个while loop，在该loop中，maker1和marker2
以不同的速度前进，若为环形链表，maker1和marker2在某次循环必定相遇，此时返回True；若不是环形，maker2或者maker1必定能到达终点，此时返回False

'''
from nose.tools import assert_equal
from linked_list import Node

def iscircular(node):
    maker1 = node
    maker2 = node

    while maker2 != None and maker2.next_node!= None:
        maker1 = maker1.next_node
        maker2 = maker2.next_node.next_node

        if maker2 == maker1:
            return True

    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a  # Cycle Here!

# CREATE NON CYCLE LIST
# 即使所有node的值（value）都相同，也能通过测试
x = Node(1)
y = Node(1)
z = Node(1)
k = Node(1)
l = Node(1)

x.next_node = y
y.next_node = z
z.next_node = k
k.next_node = l

# A test to check if the function works
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")

# Run Tests

t = TestCycleCheck()
t.test(iscircular)
##############
