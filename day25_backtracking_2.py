'''216.组合总和III

'''
class Solution(object): #my sol, 未剪枝优化
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.back_tracking(k,n,[],result,1)
        return result
    def back_tracking(self,k,n,path,result,startIndex):
        if len(path)==k and sum(path)==n:
            result.append(path[:])
            return
        elif len(path)>k or sum(path)>n:
            return
        for i in range(startIndex,10):#limiting it
            path.append(i)
            self.back_tracking(k,n,path,result,i+1)
            path.pop()

class Solution(object): #my sol. optimize by做减法而不是算和
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.back_tracking(k,n,[],result,1)
        return result
    def back_tracking(self,k,n,path,result,startIndex):
        if len(path)>k or n<0:
            return
        elif len(path)==k and n==0:
            result.append(path[:])
            return
        for i in range(startIndex,11-k+len(path)):#limiting it
            path.append(i)
            self.back_tracking(k,n-i,path,result,i+1)#n-i因为在公式里，直接做了backtracking了
            path.pop()


'''17.电话号码的字母组合

'''
class Solution(object): # my sol
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return
        result = []
        l = len(digits)
        self.phone_book = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
        '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        self.backtracking(l,digits,result,'')
        return result
    
    def backtracking(self,l,digits,result,path):
        if not digits:
            result.append(path[:])
            return
        for i in self.phone_book[digits[0]]:
            path+=i
            self.backtracking(l,digits[1:],result,path)
            path=path[:-1]

class Solution: #标准答案
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
    
    def getCombinations(self, digits, index, s):
        if index == len(digits):
            self.result.append(s)
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            self.getCombinations(digits, index + 1, s + letter)
    
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        self.getCombinations(digits, 0, "")
        return self.result