'''39. 组合总和

我举过例子，如果是一个集合来求组合的话，就需要startIndex，例如：77.组合 (opens new window)，216.组合总和III (opens new window)。

如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex，例如：17.电话号码的字母组合
'''
class Solution(object): #my sol
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(0,candidates,target,[],result)
        return result
    def backtracking(self,startIndex,candidates,target,path,result):
        if target<0:
            return
        if target==0:
            result.append(path[:])#注意要搞这个复制的操作
            return
        for i in range(startIndex,len(candidates)):
            path.append(candidates[i])
            self.backtracking(i,candidates,target-candidates[i],path,result)
            path.pop()

class Solution(object): #my sol. optimize 一下把对比 放在了for loop里面 不用进行下一个bracktracking 
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(0,candidates,target,[],result)
        return result
    def backtracking(self,startIndex,candidates,target,path,result): #或者如果加多一个element sum （而不是target-）的话要做多一层回溯
        if target==0: #终止条件
            result.append(path[:])#注意要搞这个复制的操作
            return
        for i in range(startIndex,len(candidates)): #都是target>0的情况了 剪枝的话排序，然后只要大于 就continue
            if candidates[i] <= target: #kinda 终止条件 如果不小于target就终止了
                path.append(candidates[i])
                self.backtracking(i,candidates,target-candidates[i],path,result)
                path.pop()

class Solution: #标准答案
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        self.backtracking(candidates, target, 0, [], result)
        return result
    def backtracking(self, candidates, target, startIndex, path, result):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i, path, result)
            path.pop()

'''40.组合总和II

树层去重 树枝去重
树枝可以有重
树层去重，相当于选取的同一个位置（e.g.第一个数不会是两个同样的东西）每层要去重 就是在for loop里面
important
used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
used[i - 1] == false，说明同一树层candidates[i - 1]使用过
这里直接用startIndex来去重也是可以的， 就不用used数组了。
https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#%E6%80%9D%E8%B7%AF
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.backtracking(candidates, target, [],result,0)
        return result
    def backtracking(self,candidates,target,path, result,startIndex):
        if target == 0:
            result.append(path[:])
        # target < 0 的情况在for loop里了
        for i in range(startIndex,len(candidates)):
            if i>startIndex and candidates[i-1]==candidates[i]: #i>startIndex说明是同一层的了
            #  and candidates[i-1] not in path: # we don't need to consider this because it's already in the prior loop? 层去重
                # print(candidates[i-1],candidates[i],candidates[i+1])
                continue
            if candidates[i]>target:
                break
            path.append(candidates[i])
            self.backtracking(candidates,target-candidates[i],path, result,i+1)
            path.pop()

class Solution: #标准答案 used用到


    def backtracking(self, candidates, target, total, startIndex, used, path, result):
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            # 对于相同的数字，只选择第一个未被使用的数字，跳过其他相同数字
            if i > startIndex and candidates[i] == candidates[i - 1] and not used[i - 1]:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            used[i] = True
            self.backtracking(candidates, target, total, i + 1, used, path, result)
            used[i] = False
            total -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates, target):
        used = [False] * len(candidates)
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, used, [], result)
        return result


'''131.分割回文串

'''
class Solution(object): # my sol 
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result=[]
        self.backtracking(s,result,[])
        return result
    def backtracking(self,s,result,path):
        if not s:
            result.append(path[:])
            return
        for i in range(len(s)):
            if s[:i+1] and s[:i+1]==s[i::-1]: #因为左包右不包
                path.append(s[:i+1])
                self.backtracking(s[i+1:],result,path) #也可以不i+1:,而用start index和s的区间
                path.pop()