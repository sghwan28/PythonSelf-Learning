from typing import List

'''
leetcode 33:
搜索旋转排序数组

set left, right

while left < right:
    set mid 
    if mid = target:
        return mid
        
    if mid > left:
        if target between left and mid:
            binary search the new range 
        else:
            left += 1
    
    elif mid < left:
        if target between mid +1 and right:
            binary search the new range 
        else:
            right = mid

return left if  left == target else -1        
'''

def search(nums: List[int], target: int) -> int:
    '''
    >>> search([4,5,6,7,0,1,2],0)
    4
    '''
    if not nums:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left, right =0, len(nums)-1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] > nums[left]:  # 此时左侧有序
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left += 1
        else:  #此时右侧有序
            if nums[mid + 1] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid
    return left if nums[left] == target else -1

