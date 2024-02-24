'''583. 两个字符串的删除操作

'''
class Solution(object): #my sol
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        result = 0
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                result = max(result,dp[i][j])
        if len(word1)+len(word2)==2*result:
            return 0
        return len(word1)+len(word2)-2*result


class Solution: #标准
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i #初始每个有多少元素
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]

'''72. 编辑距离

'''
class Solution(object): #my sol
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][0]=i
        for i in range(len(word1)+1):
            dp[0][i]=i
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[-1][-1]


'''编辑距离总结篇

'''
