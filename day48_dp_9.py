'''198.打家劫舍

'''
class Solution(object): # my sol
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return max(nums)
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        for i in range(2,len(dp)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[-1]

class Solution: #标准
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:  # 如果没有房屋，返回0
            return 0
        if len(nums) == 1:  # 如果只有一个房屋，返回其金额
            return nums[0]

        # 创建一个动态规划数组，用于存储最大金额
        dp = [0] * len(nums)
        dp[0] = nums[0]  # 将dp的第一个元素设置为第一个房屋的金额
        dp[1] = max(nums[0], nums[1])  # 将dp的第二个元素设置为第一二个房屋中的金额较大者

        # 遍历剩余的房屋
        for i in range(2, len(nums)):
            # 对于每个房屋，选择抢劫当前房屋和抢劫前一个房屋的最大金额
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]  # 返回最后一个房屋中可抢劫的最大金额

# 优化版本
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  # 如果没有房屋，返回0
            return 0

        prev_max = 0  # 上一个房屋的最大金额
        curr_max = 0  # 当前房屋的最大金额

        for num in nums:
            temp = curr_max  # 临时变量保存当前房屋的最大金额
            curr_max = max(prev_max + num, curr_max)  # 更新当前房屋的最大金额
            prev_max = temp  # 更新上一个房屋的最大金额

        return curr_max  # 返回最后一个房屋中可抢劫的最大金额


'''213.打家劫舍II

'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #考虑不放nums[0] 和不放nums[-1]两种情况里的最大值
        if len(nums)<=2: return max(nums)
        result1 = self.robRange(nums,0,len(nums)-2)
        result2 = self.robRange(nums,1,len(nums)-1)
        return max(result1, result2)
    def robRange(self,nums,start,end):
        prev = nums[start]
        cur = max(nums[start],nums[start+1])
        for i in range(start+2,end+1):
            temp = cur
            cur = max(cur,prev+nums[i])
            prev = temp
        return cur

class Solution: #标准
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)  # 情况二
        result2 = self.robRange(nums, 1, len(nums) - 1)  # 情况三
        return max(result1, result2)
    # 198.打家劫舍的逻辑
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end + 1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max

'''337.打家劫舍III

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = self.traversal(root)
        return max(dp)
    
    def traversal(self,root):
        if not root:
            return (0,0) #偷，不偷
        left = self.traversal(root.left)
        right = self.traversal(root.right)

        #不偷当前
        val1 = max(left)+max(right)

        #偷
        val2 = root.val + left[1] + right[1]

        return (val2, val1)