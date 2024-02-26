'''647. 回文子串

'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if not s:
            return result
        dp = [[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)): #注意这个范围,其实是从右下开始推，但是单个从左下推,所以j只能是大于i的，随着i的for loop慢慢range变大
                if s[i]==s[j]:
                    if j-i<=1:
                        # print(j,i)
                        result+=1
                        dp[i][j]=True
                    elif dp[i+1][j-1]:
                        print(i+1,j-1)
                        dp[i][j]=True
                        result+=1
        # print(dp)
        return result


class Solution: #简介版答案
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]): 
                    result += 1
                    dp[i][j] = True
        return result

class Solution: #双指针比较快
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s)) #以i为中心
            result += self.extend(s, i, i+1, len(s)) #以i和i+1为中心
        return result
    
    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res

'''516.最长回文子序列

'''
class Solution(object): # my sol
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0]*len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    if j==i:
                        dp[i][j]=1
                    elif j==i+1:
                        dp[i][j]=2
                    else:
                        dp[i][j]=dp[i+1][j-1]+2
                    result = max(dp[i][j],result)
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        # print(dp)
        return result

class Solution: #标准
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


'''动态规划总结篇

动规五部曲分别为：

确定dp数组（dp table）以及下标的含义
确定递推公式
dp数组如何初始化
确定遍历顺序
举例推导dp数组
'''