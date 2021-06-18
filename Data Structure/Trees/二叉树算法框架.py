from BinaryTree import BinaryTree

a = BinaryTree(1)
a.insertLeft(2)
a.insertRight(3)
a.insertLeft(4)

print(a.key)
print(a.leftChild.key)
print(a.leftChild.leftChild.key)


def plusone(node:BinaryTree):

    # 第一步，描述单个节点的操作
    if not node:
        return
    node.key += 1

    # 第二步，交给二叉树框架
    plusone(node.leftChild)
    plusone(node.rightChild)


plusone(a)
print(a.key)
print(a.leftChild.key)
print(a.leftChild.leftChild.key)

"""
通过两次print的结果可以看出，二叉树上所有节点都已经成功 +1
"""


"""
leetcode no.100
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val != q.val:
            return False
        # 以上代码检验单个节点

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # 代入二叉树框架运行，所有节点都为True时，两树完全相同，只要有一点不同，直接return false
