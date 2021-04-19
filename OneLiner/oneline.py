from typing import List

'''
力扣 魔术索引

示例：
输入：nums = [0, 2, 3, 4, 5]
输出：0
说明: 0下标的元素为0
'''


def FindMagicIndex(nums: List[int]) -> int:
    return next(iter(i for i, num in enumerate(nums) if i == num), -1)

# iter 召唤一个迭代器
# enumerate 排序器
# next calls on the iterator, when no items is present, it throw an error or the default value
