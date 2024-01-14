'''
一般没有返回值 void (参数) {
    if (终止条件) {收集结果}
}
单层搜索 for循环 (集合元素) {处理节点 递归，回溯}

递归函数参数 返回值
确认终止条件：path的数组的大小达到k
如果for循环选择的起始位置之后的元素个数 已经不足 我们需要的元素个数了，那么就没有必要搜索了

单层递归逻辑
'''

'''77. 组合  

'''
class Solution(object): #未剪枝优化
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(n,k,1,[],result) #[] is the empty path for now
        return result
    def backtracking(self,n,k,startIndex,path,result):
        #终止条件
        if len(path)==k:
            result.append(path[:]) #void
            return #不走for循环了
        for i in range(startIndex,n+1):
            path.append(i)
            self.backtracking(n,k,i+1,path,result)
            path.pop()
            
class Solution(object): #剪枝
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(n,k,1,[],result) #[] is the empty path for now
        return result
    def backtracking(self,n,k,startIndex,path,result):
        #终止条件
        if len(path)==k:
            result.append(path[:]) #void
            return #不走for循环了
        for i in range(startIndex,n-(k-len(path))+2): #+2因为本身就要+1
            path.append(i)
            self.backtracking(n,k,i+1,path,result)
            path.pop()
            