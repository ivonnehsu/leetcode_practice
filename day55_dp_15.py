'''392.判断子序列 

'''
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        result = 0
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if t[i-1]==s[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=dp[i-1][j] #可能j之前match过了
                result = max(result,dp[i][j])
        print(dp)
        return result == len(s)



'''115.不同的子序列
******* hard/should review
dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
用删除元素 的逻辑 i-1
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        dp[0][0]=1
        for i in range(1,len(s)+1):
            if t[0]==s[i-1]:
                dp[i-1][0]=1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
    
class Solution: #标准答案 合并
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for j in range(1, len(t)):
            dp[0][j] = 0
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]