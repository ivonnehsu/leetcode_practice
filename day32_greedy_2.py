'''122.买卖股票的最佳时机II

拆成每一天的利润
'''
class Solution(object): # my sol
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) <= 1:
            return result
        prev = prices[0]
        for i in prices[1:]:
            level = i - prev
            if level >0:
                result+=level
            prev = i
        return result

class Solution: #标准答案
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result

'''55. 跳跃游戏

#需要复习一下的
'''
class Solution(object): #切入点是覆盖范围 <= cover 而不是nums
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        coverage = 0
        if len(nums)==1: return True #漏了思考这个点，就在起始位置
        for i in range(len(nums)):
            print(coverage,i+nums[i])
            # coverage = max(coverage,i+nums[i]) <- 要先确定coverage才有这一步
            # if coverage == 0:
            #     break
            if i <= coverage: #需要在cover 范围之内
                coverage = max(i + nums[i], coverage)
                if coverage >= len(nums)-1: return True
        return False

class Solution: #另一个标准答案
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False

'''45.跳跃游戏II

'''
class Solution(object): #my sol
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return 0
        coverage = 0
        max_coverage = 0
        step = 0
        while True:
            step+=1
            for i in range(coverage+1):
                max_coverage = max(max_coverage,i+nums[i])
            if max_coverage>=len(nums)-1:
                break
            coverage=max_coverage
        return step
        
class Solution: #标准
    def jump(self, nums):
        cur_distance = 0  # 当前覆盖的最远距离下标
        ans = 0  # 记录走的最大步数
        next_distance = 0  # 下一步覆盖的最远距离下标
        
        for i in range(len(nums) - 1):  # 注意这里是小于len(nums) - 1，这是关键所在
            next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖的最远距离下标
            if i == cur_distance:  # 遇到当前覆盖的最远距离下标
                cur_distance = next_distance  # 更新当前覆盖的最远距离下标
                ans += 1
        
        return ans
