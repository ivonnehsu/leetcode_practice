'''数组part2'''
# leetcode 977 有序数组的平方
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums_1 = [i*i for i in nums]
        # return sorted(nums_1)


        # ans = len(nums) * [float('inf')]
        # left,right, n = 0, len(nums)-1, len(nums)-1
        # while left <= right:
        #     if nums[left]**2 < nums[right]**2:
        #         ans[n] = nums[right]**2
        #         right -= 1
        #     else:
        #         ans[n] = nums[left]**2
        #         left += 1
        #     n-=1
        # return ans

        start, end, n = 0, len(nums)-1, len(nums)-1
        ans = [0] * len(nums)
        # print(ans)
        while start <= end:
            if nums[start]**2 < nums[end]**2:
                # print(n)
                ans[n] = nums[end]**2
                end-=1
                n -= 1
            else:
                ans[n] = nums[start]**2
                # print(n)
                start+=1
                n -= 1
        return ans

# ans = Solution()
# print(ans.sortedSquares(nums=[-4,-1,0,3,10]))

# 注意如果要建立一个list的时候 要建立适合长度


#leetcode 209长度最小的子数组
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # left, right = 0, 0
        # minimal_len = float('inf')
        # minimal_sum = 0
        # while right < len(nums):
        #     minimal_sum+=nums[right]
        #     while minimal_sum >= target:
        #         minimal_len = min(minimal_len, right - left + 1)
        #         minimal_sum -= nums[left]
        #         left += 1
        #     right += 1
        # return 0 if minimal_len == float('inf') else minimal_len

        left = 0
        minimal_len = float('inf')
        nums_sum = 0
        for right, val in enumerate(nums):
            nums_sum += val
            while nums_sum >= target:
                minimal_len = min(minimal_len, right - left + 1)
                # print(nums_sum, minimal_len)
                nums_sum -= nums[left]
                left += 1
        return 0 if minimal_len == float('inf') else minimal_len

# ans = Solution()
# print(ans.minSubArrayLen(target= 7, nums=[2,3,1,2,4,3]))

# 注意事项在左指针和计算总和的先后顺序

# leetcode 59 螺旋数组

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # ans = [[0] * n for _ in range(n)]
        # start_x, start_y = 0, 0
        # loop, mid = n//2, n//2
        # num = 1 # starting number
        # for offset in range(1,loop+1):
        #     for i in range(start_y, n-offset):
        #         ans[start_x][i] = num
        #         num += 1
        #     for i in range(start_x, n-offset):
        #         ans[i][n-offset] = num
        #         num += 1
        #     for i in range(n-offset, start_y, -1):
        #         ans[n-offset][i] = num
        #         num += 1
        #     for i in range(n-offset, start_x, -1):
        #         ans[i][start_y] = num
        #         num += 1
        #     start_x += 1
        #     start_y += 1
        # if n%2 == 1:
        #     ans[loop][loop] = num # because starting at 0
        # return ans

        ans = [[0] * n for _ in range(n)]
        x, y = 0,0
        loops = n//2
        num = 1
        for offset in range(1, loops+1):
            for i in range(y, n-offset):
                ans[x][i] = num
                num += 1
            for i in range(x, n-offset):
                ans[i][n-offset] = num
                num += 1
            for i in range(n-offset, y, -1):
                ans[n-offset][i] = num
                num += 1
            for i in range(n-offset, x, -1):
                ans[i][y] = num
                num += 1
            x += 1
            y += 1
        if n%2 ==1:
            ans[n//2][n//2]=num
        return ans


ans = Solution()
print(ans.generateMatrix(n=3))

# 多思考步骤