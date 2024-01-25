'''1005.K次取反后最大化的数组和

'''
class Solution(object): # my sol
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        idx = 0
        while k>0:
            if idx <len(nums) and nums[idx]<0:
                nums[idx]=-nums[idx]
                idx+=1
                k-=1
            else:
                nums.sort()
                nums[0]=-nums[0]
                k-=1
        return sum(nums)

class Solution: #标准答案
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort(key=lambda x: abs(x), reverse=True)  # 第一步：按照绝对值降序排序数组A

        for i in range(len(A)):  # 第二步：执行K次取反操作
            if A[i] < 0 and K > 0:
                A[i] *= -1
                K -= 1

        if K % 2 == 1:  # 第三步：如果K还有剩余次数，将绝对值最小的元素取反
            A[-1] *= -1

        result = sum(A)  # 第四步：计算数组A的元素和
        return result

'''134. 加油站

'''




'''135. 分发糖果

'''