from linked_list import Node
'''
Question: Define a function to reverse a linked list 

The function will take in the head of the list as input and return the new head of the list

'''

def reverse(head:Node):
    current = head
    previous = None
    next = None

    while current:
        # assign the next according to the original linked list
        next = current.next_node

        # Reverse the pointer
        current.next_node = previous

        # move to the next
        # update all parameters
        previous = current
        current = next

    return previous


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

reverse(a)
# Should have no AssertionError
assert b.next_node.value == 1
assert c.next_node.value == 2
assert d.next_node.value == 3
assert a.next_node == None

