'''738.单调递增的数字

'''
class Solution(object): #my sol
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst_n = [int(i) for i in str(n)]
        if len(lst_n)==1:return n #smaller or same
        for i in range(len(lst_n)-2,-1,-1):
            if lst_n[i]>lst_n[i+1] or lst_n[i]==lst_n[i+1]==0:
                lst_n[i]=lst_n[i]-1
                lst_n[i+1:]=[9]*(len(lst_n)-i-1)
        lst_n = [str(i) for i in lst_n]
        return int(''.join(lst_n))

class Solution: #标准
    def monotoneIncreasingDigits(self, N: int) -> int:
        strNum = str(N)        
        for i in range(len(strNum) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                # 将前一个字符减1，以保证递增性质
                # 使用字符串切片操作将修改后的前面部分与后面部分进行拼接
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + '9' * (len(strNum) - i)       
        return int(strNum)

'''968.监控二叉树

'''
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if self.cameraCount(root) == 0: self.result+=1
        return self.result
    def cameraCount(self,root):
        if not root:
            return 2 #相当于有覆盖
        left = self.cameraCount(root.left)
        right = self.cameraCount(root.right)
        if left == 2 and right == 2: return 0 #他的父节点放摄像头
        if left == 0 or right == 0: #无
            self.result+=1 
            return 1 #放镜头
        elif left ==1 or right == 1: #其中一个摄像头 父节点一定是覆盖
            return 2

'''总结

'''