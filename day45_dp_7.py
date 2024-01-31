'''70. 爬楼梯 （进阶
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬至多m (1 <= m < n)个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

输入描述：输入共一行，包含两个正整数，分别表示n, m

输出描述：输出一个整数，表示爬到楼顶的方法数。

输入示例：3 2

输出示例：3

提示：

当 m = 2，n = 3 时，n = 3 这表示一共有三个台阶，m = 2 代表你每次可以爬一个台阶或者两个台阶。

此时你有三种方法可以爬到楼顶。

1 阶 + 1 阶 + 1 阶段
1 阶 + 2 阶
2 阶 + 1 阶

'''
class Solution(object): #my sol 排列数
    def climbStairs(self, m, n):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i>=j:
                    dp[i]+=dp[i-j]
        return dp[-1]


'''322. 零钱兑换

如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。
'''
class Solution(object): #my sol
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0]=0 #模拟就知道了 
        for c in coins:
            for a in range(1,amount+1): #可以直接写range(c)
                if a>=c:
                    dp[a]=min(dp[a],dp[a-c]+1)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]


class Solution: #答案
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # 创建动态规划数组，初始值为正无穷大
        dp[0] = 0  # 初始化背包容量为0时的最小硬币数量为0

        for coin in coins:  # 遍历硬币列表，相当于遍历物品
            for i in range(coin, amount + 1):  # 遍历背包容量
                if dp[i - coin] != float('inf'):  # 如果dp[i - coin]不是初始值，则进行状态转移
                    dp[i] = min(dp[i - coin] + 1, dp[i])  # 更新最小硬币数量

        if dp[amount] == float('inf'):  # 如果最终背包容量的最小硬币数量仍为正无穷大，表示无解
            return -1
        return dp[amount]  # 返回背包容量为amount时的最小硬币数量

'''279.完全平方数

'''
class Solution(object): #my version slow
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1): #nums
            for j in range(i**2,n+1):
                if dp[j-i**2]!= float('inf'):
                    dp[j]=min(dp[j],dp[j-i**2]+1)
        return dp[-1]

class Solution: #标准 先遍历物品
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, int(n ** 0.5) + 1):  # 遍历物品
            for j in range(i * i, n + 1):  # 遍历背包
                # 更新凑成数字 j 所需的最少完全平方数数量
                dp[j] = min(dp[j - i * i] + 1, dp[j])

        return dp[n]

class Solution: #先遍历背包
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):  # 遍历背包
            for j in range(1, int(i ** 0.5) + 1):  # 遍历物品
                # 更新凑成数字 i 所需的最少完全平方数数量
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]