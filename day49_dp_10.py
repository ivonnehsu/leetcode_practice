'''121. 买卖股票的最佳时机

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*2 for i in range(len(prices))] #不持有股票的最高现金，持有股票的最高现金
        dp[0][0]=-prices[0]
        dp[0][1]=0
        if not prices:
            return 0
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],-prices[i])
            dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
        return dp[-1][1]

class Solution: #更快
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp0, dp1 = -prices[0], 0 #注意这里只维护两个常量，因为dp0的更新不受dp1的影响
        for i in range(1, length):
            dp1 = max(dp1, dp0 + prices[i])
            dp0 = max(dp0, -prices[i])
        return dp1

'''122.买卖股票的最佳时机II

'''

class Solution(object): #贪心
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) <= 1:
            return result
        prev = prices[0]
        for i in prices[1:]:
            level = i - prev
            if level >0:
                result+=level
            prev = i
        return result

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*2 for i in range(len(prices))]
        dp[0][0]=-prices[0] # 0， 持有
        dp[0][1]=0 # 1，不持有
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1] [0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]