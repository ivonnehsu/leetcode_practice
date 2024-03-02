'''503.下一个更大元素II

'''
class Solution(object): # my sol
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1]*len(nums)
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(i)
            while stack and nums[i]>nums[stack[-1]]:
                result[stack[-1]]=nums[i]
                stack.pop()
            stack.append(i)
        # print(stack)
        if not stack: 
            return result
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                result[stack[-1]]=nums[i]
                stack.pop()
        return result


class Solution: # 标准
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dp = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
                    dp[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
            stack.append(i%len(nums))
        return dp

'''42. 接雨水

'''
class Solution(object): # my res, 修改了好多次
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        for i in range(len(height)):
            if not stack or height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[stack[-1]]<=height[i]:
                    l = stack.pop()
                    if stack:
                        u = stack[-1]
                        result+=((min(height[u],height[i])-height[l])*(i-u-1))
                stack.append(i)
        return result