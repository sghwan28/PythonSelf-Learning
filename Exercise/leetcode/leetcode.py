'''
83.删除链表中的重复元素
'''


# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head == None or head.next == None:
#             return head
#
#         marker1 = head  # 双指针法
#         marker2 = head.next
#         while marker2:
#             if marker1.val < marker2.val:
#                 marker1 = marker1.next
#                 marker2 = marker2.next
#             else:
#                 marker1.next = marker2.next
#                 marker2 = marker2.next
#
#         return head


'''
1. 两数之和
'''

from typing import List

# 暴力求解 算法复杂度大
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#

# Hash map 速度会快一些
#
# class Solution2:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d ={}
#         for index,value in enumerate(nums):
#             if target - value in d:
#                 return [d[target-value],index]
#             d[value] = index


'''
14.最长公共前缀
'''
# def longestCommonPrefix(strs):
#     if not strs:
#         return ''
#
#     strs.sort(key=lambda x: len(x))
#     s_min = strs[0]
#     i = 0
#     # 纵向扫描
#     for i in range(len(s_min)):
#         # 有一个不以 s_min[0:i+1] 起始 就break
#         if False in [s.startswith(s_min[0:i + 1]) for s in strs]:
#             break
#         # 如果走到了最后 且都是匹配的  因为最后一个 i=len-1 注意要+1
#         if i == len(s_min) - 1:
#             i = len(s_min)
#     return s_min[0:i]

'''
HW5. 最长回文串
'''
# 暴力求解
# def longestPalindrome(s: str) -> list[str]:
#     dp = [k for k in s]
#     for i in range(len(s)):
#         for j in range(len(s) - 1, i, -1):
#             if s[i:j + 1] == s[i:j + 1][::-1]:
#                 dp[i] = s[i:j + 1]
#                 break
#     return sorted(dp,key=lambda s:len(s))[-1]


# 中心扩散法
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res = ''
#         for i in range(len(s)):
#             s1 = self.find(s, i, i)       # 以当前字符为中心的最长回文子串
#             s2 = self.find(s, i, i+1)     # 以当前字符和下一字符为中心的最长回文子串
#             #如果最大长度有变化则更新res
#             if max(len(s1), len(s2)) > len(res):
#                 res = s2 if len(s1) < len(s2) else s1
#         return res
#
#     def find(self, s, left, right):
#         #找到当前中心的最大长度子串
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left+1:right]
#

'''
643. 子数组最大平均数
'''
# 暴力法
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         dp = [nums[o] for o in range(len(nums)-k+1)]
#
#         for i in range(len(nums)-k+1):
#             dp[i] = sum(nums[i:i+k]) / k
#         return max(dp)


# 滑动窗口 运行速度快了很多
# class Solution2:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         cur = sum(nums[:k])
#         res = cur/k
#         for i in range(k, len(nums)):
#             cur = cur - nums[i-k] + nums[i]    # 虽然总的运算次数和暴力方法一样，但滑动串口的加入大大减少了计算量，不需要多次调用sum
#             res = max(res, cur/k)
#         return res

'''
942
'''


# def diStringMatch(S: str) -> List[int]:
#     nums = list(range(len(S) + 1))
#     res = []
#     for i in S:
#         if i == 'I':
#             res.append(nums.pop(0))
#         if i == 'D':
#             res.append(nums.pop())
#
#     res.append(nums.pop())
#     return res

'''
两数相加 链表
这道题可以分裂成以下几点：

1. 链表值的相加
2. 链表长度不等问题
3. 进位问题
4. 补位问题
'''

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = ListNode(l1.val + l2.val)
#         cur = head
#
#         while l1.next or l2.next:
#             l1 = l1.next if l1.next else ListNode()   # 补长短的链表
#
#             l2 = l2.next if l2.next else ListNode()
#             cur.next = ListNode(l1.val + l2.val + cur.val // 10)    # 进位问题解决了
#             cur.val = cur.val % 10
#             cur = cur.next
#
#         if cur.val >= 10:                              # 最后补位问题
#             cur.next = ListNode(cur.val // 10)
#             cur.val = cur.val % 10
#         return head


'''
3. 无重复字符串的最长子串
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


'''
二叉树的层平均值 遍历二叉树， DFS （深度优先搜索）
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def averageOfLevels(self, root: TreeNode) -> List[float]:
#         res = []
#         if root is None: return res   # 如果初始root为空，直接返回空集
#         que = [root]    # 单向序列，先进先出
#         while que:          # 只要当前序列不为空 每次while loop都会进入下一层
#             n = len(que)         # 序列中的节点数
#             Sum = 0              #局部变量，用来记录当前层数的Sum
#             for _ in range(n):    # 需要进行n-1次加法计算
#                 cur = que.pop(0)   # 巧妙！逐渐抽空序列
#                 Sum += cur.val
#                 if cur.left: que.append(cur.left)     # 对于每个被抽出的序列，在queue中加入其子节点
#                 if cur.right: que.append(cur.right)    # 当到达最后一层时，所有cur节点都不具有子节点，while loop中止
#             res.append(Sum / n)    # for循环后把Sum提交到res（更高一级的变量中，然后进行下一level的计算
#         return res
