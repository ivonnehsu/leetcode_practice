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
class Solution(object): # my sol
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        combine = [gas[i]-cost[i] for i in range(len(gas))]
        # print(combine)
        min_val = float('inf')
        min_idx = None
        cur = 0
        for i in range(len(combine)):
            cur+=combine[i]
            if cur <= min_val:
                min_idx = i
                min_val = cur
        if min_idx == len(combine)-1:
            idx=0
        else:
            idx=min_idx+1
        return idx if sum(combine)>=0 else -1

class Solution: #标准
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(cost)):
            rest = gas[i] - cost[i]  # 记录剩余油量
            index = (i + 1) % len(cost)  # 下一个加油站的索引

            while rest > 0 and index != i:  # 模拟以i为起点行驶一圈（如果有rest==0，那么答案就不唯一了）
                rest += gas[index] - cost[index]  # 更新剩余油量
                index = (index + 1) % len(cost)  # 更新下一个加油站的索引

            if rest >= 0 and index == i:  # 如果以i为起点跑一圈，剩余油量>=0，并且回到起始位置
                return i  # 返回起始位置i

        return -1  # 所有起始位置都无法环绕一圈，返回-1
'''135. 分发糖果

'''
class Solution(object): # my codes
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result_left = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                result_left[i]=result_left[i-1]+1
        
        result_right = [1]*len(ratings)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                result_right[i]=result_right[i+1]+1
        return sum([max(result_right[i],result_left[i]) for i in range(len(ratings))])

class Solution: #标准答案 不要同时比较
    def candy(self, ratings: List[int]) -> int:
        candyVec = [1] * len(ratings)
        
        # 从前向后遍历，处理右侧比左侧评分高的情况
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyVec[i] = candyVec[i - 1] + 1
        
        # 从后向前遍历，处理左侧比右侧评分高的情况
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candyVec[i] = max(candyVec[i], candyVec[i + 1] + 1)
        
        # 统计结果
        result = sum(candyVec)
        return result