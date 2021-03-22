# Singly Linked List Implementation

# 优点1：对于数组来说，插入和删除的算法复杂度为O(n)。对于链表而言，需要的时间为常数K
# 优点2：链表可以持续扩张，无需再次声明数据结构的容量 参考 array.py 中 capacity 这个 attribute

# 缺点1：获取链表中第k个元素需要O(k)时间，对于数组而言，获取元素值的时间是O(1).
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next_node =None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next_node = b
# b.next_node = c
#
# assert a.next_node.value == 2


# Doubly Linked List Implementation
class DoublyLinkedListNode(object):
    def __init__(self,value):
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
