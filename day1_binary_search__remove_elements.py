# leetcode 704 二分查找
# https://leetcode.com/problems/binary-search/description/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
        
# # test case
# ans = Solution()
# print(ans.search(nums=[-1,0,3,5,9,12], target=9))

'''notes
1. 左闭右闭
left<=right, then right = len(nums) - 1, 
if (nums[middle] > target) right = middle - 1

2. 左闭右开
left<right, then right = len(nums)
if (nums[middle] > target) right = middle (because right can't be arrived)
'''


# leetcode 27 移除元素
# https://leetcode.com/problems/remove-element/description/

'''直接方式'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast in nums: # since the length of elements are confirmed, we can also use for loop here
            '''for loop is faster than while loop'''
            if fast != val:
                nums[slow] = fast
                # print(fast,slow)
                slow += 1
        return slow

'''双指针法'''
class Solution1(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow, fast = 0, 0
        while fast < len(nums): #类似二分法， 不加等号因为到不了
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1 # it adds after changing the value, so no need to +1 in 'return'
            fast += 1
        return slow

# # test case
# ans = Solution1()
# print(ans.removeElement(nums=[3,2,2,3], val=3))