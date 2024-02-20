'''300.最长递增子序列

'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1]*len(nums) #dp[i] 以i结尾的最长的数组
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
        return max(dp)

'''674. 最长连续递增序列

'''
class Solution(object): #my sol
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
            result=max(result,dp[i])
        return result

class Solution(object): #my sol
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 1
        dp = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp+=1
                result=max(result,dp)
            else:
                dp=1
        return result

'''718. 最长重复子数组

'''
class Solution(object): #my sol
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if not nums1 or not nums2:
            return 0
        dp = [[0]*len(nums2) for _ in range(len(nums1))]
        result = 0
        for i in range(len(nums1)):
            if nums1[i]==nums2[0]:
                dp[i][0]=1
                result = 1
        for i in range(len(nums2)):
            if nums2[i]==nums1[0]:
                dp[0][i]=1
                result = 1
        for i in range(1,len(nums1)):
            for j in range(1,len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                    result = max(result,dp[i][j])
        return result
