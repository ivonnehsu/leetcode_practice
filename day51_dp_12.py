'''309.最佳买卖股票时机含冷冻期

'''
class Solution(object): # my sol
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        dp = [[0,0] for i in range(len(prices)+1)]
        dp[1] = [-prices[0],0] #买，没买
        dp[2][0] = max(dp[1][0],-prices[1])
        dp[2][1] = max(0,-prices[0]+prices[1])
        if len(prices)==2:
            result =  prices[1]-prices[0]
            return 0 if result <0 else result
        for i in range(3,len(prices)+1):
            dp[i][0] = max(dp[i-1][0],dp[i-2][1]-prices[i-1])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i-1])
        print(dp)
        return dp[-1][1]



from typing import List

class Solution: #标准
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 4 for _ in range(n)]  # 创建动态规划数组，4个状态分别表示持有股票、不持有股票且处于冷冻期、不持有股票且不处于冷冻期、不持有股票且当天卖出后处于冷冻期
        dp[0][0] = -prices[0]  # 初始状态：第一天持有股票的最大利润为买入股票的价格
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][3], dp[i-1][1]) - prices[i])  # 当前持有股票的最大利润等于前一天持有股票的最大利润或者前一天不持有股票且不处于冷冻期的最大利润减去当前股票的价格
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])  # 当前不持有股票且处于冷冻期的最大利润等于前一天持有股票的最大利润加上当前股票的价格
            dp[i][2] = dp[i-1][0] + prices[i]  # 当前不持有股票且不处于冷冻期的最大利润等于前一天不持有股票的最大利润或者前一天处于冷冻期的最大利润
            dp[i][3] = dp[i-1][2]  # 当前不持有股票且当天卖出后处于冷冻期的最大利润等于前一天不持有股票且不处于冷冻期的最大利润
        return max(dp[n-1][3], dp[n-1][1], dp[n-1][2])  # 返回最后一天不持有股票的最大利润



'''714.买卖股票的最佳时机含手续费

'''
class Solution(object): # my sol
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0,0] for i in range(len(prices))]
        dp[0][0]=-prices[0] #have stocks
        # dp[0][1]=0 #no stocks
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)
        return max(dp[-1])

class Solution(object): # my sol., 简化成两个数和temp
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0,0]
        dp[0]=-prices[0] #have stocks
        # dp[0][1]=0 #no stocks
        for i in range(1,len(prices)):
            temp = dp[0]
            dp[0]=max(dp[0],dp[1]-prices[i])
            dp[1]=max(dp[1],temp+prices[i]-fee)
        return max(dp)