'''完全背包

每个物品可以使用无数次
01背包： dp[j]=max(dp[j],dp[j-stone]+stone) 遍历物品->倒叙遍历背包
完全背包：遍历物品->遍历背包，顺序都可以颠倒


背包最大重量为4。

物品为：

重量	价值
物品0	1	15
物品1	3	20
物品2	4	30
每件商品都有无限个！

问背包能背的物品最大价值是多少？
'''
def test_CompletePack(weight, value, bagWeight): #先遍历物品
    dp=[0]*(bagWeight+1)
    for w in range(len(weight)):
        for i in range(weight[w],bagWeight+1):
            dp[i]=max(dp[i],dp[i-weight[w]]+value[w])
    return dp[-1]

def test_CompletePack(weight, value, bagWeight): #先遍历背包
    dp=[0]*(bagWeight+1)
    for i in range(1,bagWeight+1):
        for j in range(len(weight)):
            if i>=weight[j]:
                dp[i]=max(dp[i],dp[i-weight[j]]+value[j])
    return dp[-1]

if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    result = test_CompletePack(weight, value, bagWeight)
    print(result)


'''518. 零钱兑换 II

先循环物品： 是组合
先循环目标：是排列问题 （1，2 和2，1 会都有）

在求装满背包有几种方案的时候，认清遍历顺序是非常关键的。

如果求组合数就是外层for循环遍历物品，内层for遍历背包。

如果求排列数就是外层for遍历背包，内层for循环遍历物品。
'''
class Solution(object): #my sol 第一个数为1 （组成0有1 种方法）
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0]*(amount+1)
        dp[0]=1
        for i in coins:
            for j in range(1,amount+1):
                if j >= i:
                    dp[j]+=dp[j-i]
        return dp[-1]

class Solution: #标准
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

'''377. 组合总和 Ⅳ

原理类似于爬楼梯 --- 求排列问题
'''
class Solution(object): #my sol 排列数
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for n in nums:
                if i>=n:
                    dp[i]+=dp[i-n]
        return dp[-1]