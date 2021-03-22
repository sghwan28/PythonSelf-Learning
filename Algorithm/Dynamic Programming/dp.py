# 动态规划1： 零钱分配
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

