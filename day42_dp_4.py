'''01背包问题，你该了解这些！

有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
https://programmercarl.com/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.html#%E6%80%9D%E8%B7%AF
'''
def test_2_wei_bag_problem1(weight, value, bagweight):
    dp = [[0]*(bagweight+1) for _ in range(len(weight))]
    # for i in range(len(weight)):
    #     dp[i][0]=0
    # for i in range(len(bagweight+1)):
    #     if i>=value[0]:dp[0][i]=value[0]
    #     else: dp[0][i]=0

    # 初始化
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]


    for i in range(1,len(weight)): # weight数组的大小就是物品个数
        for j in range(1,bagweight+1):  # 遍历背包容量
            if j<weight[i]: #重量与重量相比
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i]) #注意是j-weight[i]
    return dp[-1][-1]

if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_2_wei_bag_problem1(weight, value, bagweight)
    print(result) #35


'''01背包问题，你该了解这些！ 滚动数组

'''
def test_1_wei_bag_problem(weight, value, bagWeight):
    dp = [0]*(bagWeight+1)
    for i in range(len(weight)):
        for j in range(bagWeight,weight[i]-1,-1): #assuming weight >=1
            dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
    return dp[bagWeight]

if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_1_wei_bag_problem(weight, value, bagweight)
    print(result)


'''416. 分割等和子集

01背包 （只能使用一次）
相当于背包问题 是否能装满1/2
'''
class Solution(object): #my sol
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total,remaining = sum(nums)/2,sum(nums)%2
        # print(total,remaining)
        if remaining!=0: return False
        dp=[0]*(total+1) #初始成非负正数的最小值 （因为压缩 要用上一层的）
        for i in range(len(nums)):
            for j in range(total,nums[i]-1,-1): #j要大于nums[i]-1  要不然是放不进去的
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
                # print(dp[j])
        return dp[-1]==total