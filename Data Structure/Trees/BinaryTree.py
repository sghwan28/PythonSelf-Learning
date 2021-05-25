'''
满二叉树 （Full Binary Tree): 每个节点都只有0或者2个子节点
完全二叉树 (Complete Binary Tree): 除了最后一层，所有的level都完全充满，
最后一层需要尽量从左向右排，二叉堆就是一种完全二叉树
完美二叉树 （Perfect Binary Tree): 在满二叉树的基础上，所有level都被充满，完美二叉树即是满二叉树，
又是完全二叉树

'''
# Implementing the representation of a tree as a class with nodes and references


class BinaryTree(object):
    def __init__(self,root0):
        self.key = root0
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if not self.leftChild:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)        # 此处建议画图自行理解一下！
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if not self.rightChild:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    @property
    def right_child(self):
        return self.rightChild

    @property
    def left_child(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    @property
    def root_val(self):
        return self.key

'''
运行以下代码查看结果
'''

# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

'''
Below is a representation of a Tree using a list of lists. 
'''

def BinaryTree2(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 2:
        root.insert(2,[newBranch,t,[]])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def seRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

#
# # 尝试运行以下代码
# a = BinaryTree2(0)
# b = insertRight(a,1)
# print(b)
# b = insertLeft(b,1)
# print(b)
# print(getRightChild(b))