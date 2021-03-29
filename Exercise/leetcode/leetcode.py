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
def longestCommonPrefix(strs):
    if not strs:
        return ''

    strs.sort(key=lambda x: len(x))
    s_min = strs[0]
    i = 0
    # 纵向扫描
    for i in range(len(s_min)):
        # 有一个不以 s_min[0:i+1] 起始 就break
        if False in [s.startswith(s_min[0:i + 1]) for s in strs]:
            break
        # 如果走到了最后 且都是匹配的  因为最后一个 i=len-1 注意要+1
        if i == len(s_min) - 1:
            i = len(s_min)
    return s_min[0:i]


'''
1480. 一位数组动态和,一次遍历
'''
def runningSum(nums):
    res = [nums[0]]
    for i in range(1, len(nums)):
        total = res[i - 1] + nums[i]
        res.append(total)
    return res

'''
最大自序和   #动态规划
'''


def maxSubArray(self, nums: List[int]) -> int:
    dp = [i for i in nums]

    for i in range(len(nums)):
        memo = [nums[i]]
        for j in range(i + 1, len(nums)):
            memo.append(memo[-1] + nums[j])
            if memo[-1] <= 0:
                dp[i] = memo[-2]
                break
        dp[i] = max(memo)

    return max(dp)