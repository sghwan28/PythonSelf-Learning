'''
剑指 Offer 03. 数组中重复的数字
'''
class Solution:
    def findRepeatNumber(self, nums) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1

# 思路2：原地交换
# 有前提条件 题目声明了数组内数字的范围 0到n-1


class Solution2:
    def findRepeatNumber(self, nums) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
