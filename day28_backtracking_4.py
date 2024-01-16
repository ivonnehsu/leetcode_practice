'''93.复原IP地址

'''
class Solution(object): # my sol
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.backtracking(s,result,[])
        return result
    def backtracking(self,s,result,path):
        if not s and len(path)==4:
            result.append('.'.join(path))
            return
        for i in range(4):
            if i>0 and s[0]=='0':
                continue
            if len(s)<i+1:
                break
            if 0<=int(s[:i+1])<=255:
                if len(path)>3:
                    continue
                path.append(s[:i+1])
                self.backtracking(s[i+1:],result,path)
                path.pop()

class Solution: #标准
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        self.backtracking(s, 0, [], results)
        return results

    def backtracking(self, s, index, path, results):
        if index == len(s) and len(path) == 4:
            results.append('.'.join(path))
            return

        if len(path) > 4:  # 剪枝
            return

        for i in range(index, min(index + 3, len(s))):
            if self.is_valid(s, index, i):
                sub = s[index:i+1]
                path.append(sub)
                self.backtracking(s, i+1, path, results)
                path.pop()

    def is_valid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 0开头的数字不合法
            return False
        num = int(s[start:end+1])
        return 0 <= num <= 255

'''78.子集

'''
class Solution(object): # my sol
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(nums,[],result)
        return result
    def backtracking(self,nums,path,result):
        result.append(path[:]) #收获结果在终止结果上面
        if not nums: # 可以省略
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtracking(nums[i+1:],path,result)
            path.pop()

'''90.子集II

'''
class Solution(object): #my sol
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result =[]
        self.backtracking(nums,result,[])
        return result
    def backtracking(self,nums,result,path):
        result.append(path[:])
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: #(1,2,2)第一层 2 就会去重
                continue
            path.append(nums[i])
            self.backtracking(nums[i+1:],result,path)
            path.pop()