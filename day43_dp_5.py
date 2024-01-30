'''1049. 最后一块石头的重量 II

'''
class Solution(object): #my sol
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)//2 # the smaller end
        dp = [0]*(total+1)
        for stone in stones:
            for j in range(total,stone-1,-1):
                dp[j]=max(dp[j],dp[j-stone]+stone)
        return sum(stones)-dp[-1]-dp[-1]



'''494. 目标和

dp[j] 表示：填满j（包括j）这么大容积的包，有dp[j]种方法

只要搞到nums[i]，凑成dp[j]就有dp[j - nums[i]] 种方法。

例如：dp[j]，j 为5，

已经有一个1（nums[i]） 的话，有 dp[4]种方法 凑成 容量为5的背包。
已经有一个2（nums[i]） 的话，有 dp[3]种方法 凑成 容量为5的背包。
已经有一个3（nums[i]） 的话，有 dp[2]中方法 凑成 容量为5的背包
已经有一个4（nums[i]） 的话，有 dp[1]中方法 凑成 容量为5的背包
已经有一个5 （nums[i]）的话，有 dp[0]中方法 凑成 容量为5的背包
'''
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if (target+sum(nums))%2!=0 or abs(target)>sum(nums): return 0 #can be negative target
        half = (target+sum(nums))//2
        dp=[0]*(half+1)
        #### 当目标和为0时，只有一种方案，即什么都不选
        dp[0]=1
        for num in nums:
            for j in range(half,num-1,-1):
                dp[j]+= dp[j-num] # 定了nums[i]之后，不确定的需要满足和的值为j-nums[i], dp()就是它多样性的可能性， that's also why num start from the beginning? (small to large)
        return dp[-1]




'''474.一和零

'''
class Solution(object): #my sol terrible runtime
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dic = [Counter(s) for s in strs] #can't use counter because it might not have a number
        dp = [[0]*(m+1) for _ in range(n+1)]
        for item in dic:
            for j in range(n,item['1']-1,-1):
                for k in range(m,item['0']-1,-1):
                    dp[j][k]=max(dp[j][k],dp[j-item['1']][k-item['0']]+1)

        return dp[n][m]



class Solution(object): #标准
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dic = [Counter(s) for s in strs] #can't use counter because it might not have a number
        dp = [[0]*(m+1) for _ in range(n+1)]
        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for j in range(n,ones-1,-1):
                for k in range(m,zeros-1,-1):
                    dp[j][k]=max(dp[j][k],dp[j-ones][k-zeros]+1)

        return dp[n][m]