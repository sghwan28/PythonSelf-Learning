# # 动态规划1： 零钱分配
def coinChange(coins, amount):
# 数组大小为 amount + 1，初始值也为 amount + 1
# 因为总的零钱个数不会超过amount,所以初始化amount + 1即可
# 初始化值只要大于amount即可 比如amount +5，最后程序运行结果也是一样的

    # dp[i] = x 表示，当目标金额为i时，至少需要x枚硬币
    dp = [amount + 1 for _ in range(amount + 1)]
    print(dp)
    dp[0] = 0   # 0元时， 不需要任何硬币，状态转移方程中的第一种情况
    # 外层 for循环， 填充dp数组
    for i in range(len(dp)):
        #  内层 for循环，求解的是所有子问题 + 1 的最小值
        for coin in coins:
            # 子问题无解，跳过    状态转移方程中的第二种情形
            if i - coin < 0:
                continue
            dp[i] = min(dp[i],1+dp[i-coin])   # 状态转移方程中的第三种情形
    if dp[amount] == amount + 1:   # 等于初始化数值，说明无解
        return -1
    else:
        return dp[amount]

# print(coinChange([2],4))
# expected: 2

# 动态规划2： 最长上升子序列/梅花桩
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
def lengthoflis(l:list):
    if not list:
        return 0
    dp = [1 for _ in range(len(l))]   # 初始化dp数组
    dp[0] = 1
    print(dp)
    for i in range(len(l)):
        for j in range(i):
            if l[j] >= l[i]:
                continue
            dp[i] = max(dp[i], dp[j] + 1)
    print(dp)

# lengthoflis([2,5,1,5,4,5])
# expected result : 3


'''
动态规划3：合唱队 HJ24 牛客网 华为机试

这个题其实就是双向版本的最大上升子序列问题，需要从左往右排一此，再从右往左排一次
'''

def foo24(l:list):
    dp = [1 for _ in range(len(l))]
    for i in range(len(l)):
        for j in range(i):
            if l[j] < l[i] and dp[i] < dp[j] + 1:   # 优化了这段代码，运行速度比之前快了一些，不需要用到max了
                dp[i] = dp[j] + 1      # 算法复杂度任为O（n^2)
    return dp

while 1:
    try:
        n = int(input())
        lis = list(map(int,input().split()))
        a = foo24(lis)
        b = foo24(lis[::-1])[::-1]
        res = [sum(i)-1 for i in zip(a,b)]
        print(n - max(res))
    except:
        break


'''
动态规划4 ： 最长上升子序列的优化解法
以下是一种再次优化过的方法，大大降低了算法复杂度
该方法的算法复杂度为O（nLog n）

bisect module 
'''

import bisect
def foo24new(lists):
    list_num = []
    list_max = []
    for i in lists:
        local = bisect.bisect_left(list_num, i)   # bisect 会返回对有序数组a插入i时，i所在的位置（维持排序，如果重复值，排在靠左）
        if local == len(list_num):
            list_num.append(i)
            list_max.append(local+1)
        else:
            list_num[local] = i         # 不一定是准确的上升序列 但是长度会一直对应当前的最长上升序列
            list_max.append(local+1)    # dp数组
    return list_max

while 1:
    try:
        n = int(input())
        lis = list(map(int, input().split()))
        a = foo24new(lis)
        b = foo24new(lis[::-1])[::-1]
        print(n - max(map(sum, zip(a, b))) + 1)
    except:
        break