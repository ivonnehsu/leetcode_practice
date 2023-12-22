from collections import deque, Counter
from typing import List
'''239. 滑动窗口最大值

队列的应用
需要自己构造单调函数
最好先看视频
'''
class Solution(object): # my solution, exceed time limit
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        wind = deque(nums[:k])
        ans = [max(wind)]
        max_num = max(wind)
        for i in range(k,len(nums)):
            l = wind.popleft()
            r = nums[i]
            wind.append(r)
            print(wind)
            if max_num<r:
                max_num = r
            elif max_num>r and max_num!=l:
                pass
            else:
                max_num = max(wind)
            ans.append(max_num)
            print(ans)
        return ans

# temp = Solution()
# print(temp.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


# adjusted O(n) runtime
class SingleQue():
    def __init__(self):
        self.que = deque()
    def push(self,value):
        while self.que and self.que[-1]<value: #相当于只想要保留最大的值 别的没所谓
            self.que.pop()
        self.que.append(value)
    def pop_left(self,value):
        if self.que and self.que[0]==value: # 注意if 还是 while
            self.que.popleft()
    def return_max(self):
        return self.que[0]
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sol = SingleQue()
        sol_lst = []
        for i in range(k):
            sol.push(nums[i])
        sol_lst.append(sol.return_max())
        for i in range(k,len(nums)):
            sol.pop_left(nums[i-k])
            sol.push(nums[i])
            sol_lst.append(sol.return_max())
        return sol_lst

'''347.前 K 个高频元素

仔细审题，回复key
'''
class Solution(object): # my solution, wrong
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct = Counter(nums)
        print(ct)
        ans = []
        for key, i in ct.items():
            temp = deque()
            while ans and ans[-1]<i:
                temp.append(ans.pop())
            print(temp)
            if len(ans)<k:
                ans.append(i)
            while temp and len(ans)<k:
                ans.append(temp.pop())
            print(ans)
        return k.keys 

temp = Solution()
print(temp.topKFrequent([1,1,1,2,2,3],2))

# 大顶堆，小顶堆
# 大顶堆：从大到小的排序， 小顶堆，从小到大排序
# Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
# heap[0] is the smallest item
# https://docs.python.org/3/library/heapq.html
#时间复杂度：O(nlogk)
#空间复杂度：O(n)

# the objective can simply be a []

# heapq.heappush(heap, item)
## Push the value item onto the heap, maintaining the heap invariant.

# heapq.heappop(heap)
## Pop and return the smallest item from the heap, maintaining the heap invariant. 
## If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].


import heapq

class Solution: #标准答案
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率, 也可以用counter
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result