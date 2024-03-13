'''
also in day8_string01
'''



'''11. Container With Most Water

'''
class Solution(object): # my sol, both point need to move
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        result = 0
        right = len(height)-1
        while left < right:
            l = right - left
            if height[left]<height[right]:
                result = max(result,l*height[left])
                left+=1
            else:
                result = max(result,l*height[right])
                right-=1
        return result



'''15. 3Sum

'''
class Solution(object): # very slow, run time, my sol
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    result.add(tuple([nums[i],nums[l],nums[r]]))
                if nums[i]+nums[l]+nums[r]<=0:
                    l+=1
                else:
                    r-=1
        return list(result)


'''16. 3Sum Closest

'''
class Solution(object): # my sol
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = float('inf')
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if abs(target-total)<abs(target-result):
                    result = total
                if total<target:
                    l+=1
                else:
                    r-=1
        return result
                    



'''31. Next Permutation

need to review

'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i-=1
        if i == 0:
            nums.reverse()
            return
        while nums[j] <= nums[i-1]:
            j-=1
        nums[j], nums[i-1] = nums[i-1], nums[j]
        l,r = i, len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1



'''1048. Longest String Chain

could use dp
'''


''' prev = "chain"
To build all possible successors, we need to add a letter anywhere in the word.
_ c _ h _ a _ i _ n _
We have 6 possible spaces and 26 possible letters, so a total of 6 * 26 possibilities.

Now, getting a predecessor from a word is a lot easier. Just remove a letter.
word = "chains"
pred = {"hains", "cains", "chins", "chans", "chais", "chain"}
'''
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 从小到大 但每一个用大的和小的比
        dp = dict()
        result = 1
        words.sort(key=len)
        # print(words)
        for word in words:
            dp[word]=1 # 如果有重复的，不能用+=
            for j in range(len(word)):
                sub = word[:j]+word[j+1:]
                if sub in dp:
                    dp[word]=max(dp[word],dp[sub]+1)
                    result = max(result,dp[word])
        return result
        