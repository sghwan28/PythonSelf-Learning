'''
Binary Heap
二叉堆

二叉堆有堆的性质，即父节点的值总是大于等于或者小于等于子节点
同时又具有二叉树的性质，每个节点最多有2个子节点

Heaps are commonly implemented with an array. Any binary tree can be stored in an
array, since a binary heap is always a complete binary tree, it can be stored compactly.

'''

# Implementation of a Binary Heap

class BinHeap(object):
    def __init__(self):
        self.heapList =[0]
        self.currentSize = 0

    def percUp(self,i):  #This is to maintain the heap structure after each insertion
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:    # Less than its parent node
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2    # 向上扩张

    def insert(self,k):  # k is the value of the node, i refers to the index in the list
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def minChild(self,i):  # return the index of the minimum child of a node
        if i*2 +1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def percDown(self,i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]

            i = mc   # i向下扩张

    def delMin(self):   # in this case, the root node is must the minimum
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2   # here i refers to the parent node
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1








