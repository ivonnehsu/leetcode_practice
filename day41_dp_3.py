'''
dp数组和下表含义
递推公式+dp数组初始化+遍历顺序+打印dp数组
'''

'''343. 整数拆分


要十分理清dp数组和下标的含义
'''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0],dp[1],dp[2]=0,0,1
        for i in range(3,n+1):
            for j in range(1,i//2+1):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]


'''96.不同的二叉搜索树

'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            for j in range(1,i+1): #j 作为头
                # print(i,j)
                dp[i]+=dp[j-1]*dp[i-j] #j的左边有多少个，右边多少个
        return dp[n]