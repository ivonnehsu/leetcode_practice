'''123.买卖股票的最佳时机III

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*4 for i in range(len(prices))]
        if not prices:
            return 0
        dp[0][0]=-prices[0] #第一次入
        dp[0][2]=-prices[0] #第二次入
        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]-prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]+prices[i])
        return dp[-1][3]
        

class Solution: # easier solution, just one round and keep replacing
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [0] * 5 
        dp[1] = -prices[0]
        dp[3] = -prices[0]
        for i in range(1, len(prices)):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        return dp[4]


'''188.买卖股票的最佳时机IV

'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0]*(2*k+1)
        for x in range(2*k+1):
            if x%2==1:
                dp[x]=-prices[0]
        for i in range(1,len(prices)):
            for x in range(1,2*k+1):
                if x%2 ==1:
                    dp[x]=max(dp[x],dp[x-1]-prices[i]) #买进
                else:
                    dp[x]=max(dp[x],dp[x-1]+prices[i]) #卖出
        return dp[-1]
