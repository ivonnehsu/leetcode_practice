'''62.不同路径

'''
class Solution(object): #my sol要分清楚m和n的方向
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
        for i in range(m):
            dp[0][i]=1
        for j in range(1,n):
            for k in range(1,m):
                dp[j][k]=dp[j-1][k]+dp[j][k-1]
        return dp[n-1][m-1]


'''63. 不同路径 II

'''
class Solution(object): # my sol
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        
        dp=[[0]*n for _ in range(m)]
        default=1
        for i in range(n):
            if obstacleGrid[0][i]==1:
                default=-1
            dp[0][i]=default
        default=1
        for i in range(m):
            if obstacleGrid[i][0]==1:
                default=-1 #没必要负数 变0 break就好了
            dp[i][0]=default
        #print(dp)
        for j in range(1,m):
            for k in range(1,n):
                if obstacleGrid[j][k]==1:
                    dp[j][k]=-1
                elif dp[j-1][k]==-1:
                    dp[j][k]=dp[j][k-1]
                elif dp[j][k-1]==-1:
                    dp[j][k]=dp[j-1][k]
                else:
                    dp[j][k]=dp[j][k-1]+dp[j-1][k]
        return 0 if dp[m-1][n-1]==-1 else dp[m-1][n-1]

class Solution: #标准答案 
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:  # 遇到障碍物时，直接退出循环，后面默认都是0
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]