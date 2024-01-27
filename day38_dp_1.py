'''理论基础
dp数组和下表含义
递推公式+dp数组初始化+遍历顺序+打印dp数组
'''


'''509. 斐波那契数

'''
class Solution(object): # my sol 递归
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)


class Solution(object): #method for dp
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0 #corner case
        dp = [0]*(n+1) #since there's num on f(0) it's actulaly no.n+1
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

'''70. 爬楼梯

确认爬到第一级和第二级的方法。爬到第三级只可能第一级走两级或者第二级走一级。所以可能性是肯定的，就是前两个相加
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # consider the edge case
        if n==1: return 1
        dp = [0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]


# 空间复杂度为O(3)版本
class Solution: #标准
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * 3 #为了凑成数组 把dp[0]定义成0不影响计算
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total
        
        return dp[2]

'''746. 使用最小花费爬楼梯

'''
class Solution(object): #my sol
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=0
        # dp[2]=min(dp[0]+cost[0],dp[1]+cost[1])
        for i in range(2,n+1):
            dp[i]=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[n]
