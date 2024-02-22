'''1143.最长公共子序列

'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return None
        if len(text2)>len(text1):
            text1, text2 = text2, text1
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        result = 0
        for i in range(1,len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                result = max(result,dp[i][j])
        return result


'''1035.不相交的线

'''
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if not nums1 or not nums2:
            return 0
        dp = [[0]*(len(nums1)+1) for _ in range(len(nums2)+1)]
        result = 0
        for i in range(1,len(nums2)+1):
            for j in range(1,len(nums1)+1):
                if nums2[i-1]==nums1[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
            result = max(result,dp[i][j])
        return result


'''53. 最大子序和  动态规划

'''
class Solution(object): # my sol
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 负数的话就直接重新开始（因为只会让后面的数更小）
        # cur_sum = 0
        # result = float('-inf')
        # for i in nums:
        #     # if cur_sum==0 and i<=0:
        #     #     cur_sum+=i
        #     if cur_sum<0: #无论i是否>0,都重新开始
        #         cur_sum=i
        #     else:
        #         cur_sum+=i
        #     result=max(cur_sum,result)
        # return result
        if not nums:
            return 0
        dp = [float('-inf')]*len(nums)
        dp[0]=nums[0]
        result = dp[0]
        for i in range(1,len(nums)):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
            result = max(result,dp[i])
        return result


class Solution(object): #my sol, 合并 max()
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # 负数的话就直接重新开始（因为只会让后面的数更小）
        # cur_sum = 0
        # result = float('-inf')
        # for i in nums:
        #     # if cur_sum==0 and i<=0:
        #     #     cur_sum+=i
        #     if cur_sum<0: #无论i是否>0,都重新开始
        #         cur_sum=i
        #     else:
        #         cur_sum+=i
        #     result=max(cur_sum,result)
        # return result
        if not nums:
            return 0
        dp = [float('-inf')]*len(nums)
        dp[0]=nums[0]
        result = dp[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            result = max(result,dp[i])
        return result