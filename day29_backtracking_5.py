'''491.递增子序列

'''
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(nums,result,[])
        return result
    def backtracking(self,nums,result,path):
        if len(path)>1:
            result.append(path[:])
        for i in range(len(nums)):
            if not path or nums[i]>=path[-1]: #保证了是递增
                if i>0 and nums[i] in nums[:i]: #i>0 meaning it's on 树层 nums[:i]因为不是按顺序的 所以要确保前面都没有
                    continue
                path.append(nums[i])
                self.backtracking(nums[i+1:],result,path)
                path.pop()

class Solution(object): #my sol 用set
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(nums,result,[])
        return result
    def backtracking(self,nums,result,path):
        if len(path)>1:
            result.append(path[:])
        temp = set()
        for i in range(len(nums)):
            if not path or nums[i]>=path[-1]: #保证了是递增
                if temp and nums[i] in temp: #i>0 meaning it's on 树层 nums[:i]因为不是按顺序的 所以要确保前面都没有
                    continue
                temp.add(nums[i])
                path.append(nums[i])
                self.backtracking(nums[i+1:],result,path)
                path.pop()

class Solution: #标准答案
    def findSubsequences(self, nums):
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result
    
    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:
            result.append(path[:])  # 注意要使用切片将当前路径的副本加入结果集
            # 注意这里不要加return，要取树上的节点
        
        uset = set()  # 使用集合对本层元素进行去重
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset: #主要是这里不同 优化了
                continue
            
            uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()

'''46.全排列

'''
class Solution(object): #my sol 0，1可以改成t/f
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        mapping = [0]*len(nums)
        self.backtracking(nums,result,[],mapping)
        return result
    def backtracking(self,nums,result,path,mapping):
        if sum(mapping)==len(nums): # len(path)==len(nums)也是的
            result.append(path[:])
            return
        for i in range(len(nums)):
            if mapping[i]==1: #==1可以省略
                continue
            mapping[i]=1
            path.append(nums[i])
            self.backtracking(nums,result,path,mapping)
            mapping[i]=0
            path.pop()

'''47.全排列 II

'''
class Solution(object): #my sol
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        mapping = [False]*len(nums)
        self.backtracking(nums,result,[],mapping)
        return result
    def backtracking(self,nums,result,path,mapping):
        if len(nums)==len(path):
            result.append(path[:])
            return
        temp=set()
        for i in range(len(nums)):
            if nums[i] in temp or mapping[i]:
                continue
            temp.add(nums[i])# 这是一层的 所以之后不用backtrack
            path.append(nums[i])
            mapping[i]=True #这是跟随一路的
            self.backtracking(nums,result,path,mapping)
            path.pop()
            mapping[i]=False