"""
leetcode 84: 柱状图中最大的矩形

"""

from typing import List


def largestRectangleArea(heights: List[int]) -> int:

    maxarea = 0
    stk = list()

    for i in range(len(heights)):
        # 只要栈不为空，并且当前遍历的数据小于栈顶元素，则说明找到了右边界
        while stk and heights[i] < heights[stk[-1]]:
            h = heights[stk[-1]]
            stk.pop()
            # 出栈后，如果栈为空，说明出栈的柱子目前遍历的最短的柱子，否则计算宽度差
            w = i - stk[-1] - 1 if stk else i
            maxarea = max(h * w, maxarea)
        # 栈为空或者当前遍历的数据大于等于栈顶数据，则入栈，不会执行上面的while循环
        # 保证了栈中的数据总是递增的 比如  0 1 2 2 3 4 4 5 6 ...
        stk.append(i)

    # 处理剩余栈中的数据(递增的数据，右边界是柱状图中最右边的柱子)
    while stk:
        h = heights[stk[-1]]
        stk.pop()
        # 出栈后，如果栈为空，说明出栈的柱子目前遍历的最短的柱子，否则计算宽度差
        w = len(heights) - stk[-1] - 1 if stk else len(heights)
        maxarea = max(h * w, maxarea)

    return maxarea

print(largestRectangleArea([2,1,5,6,2,3]))