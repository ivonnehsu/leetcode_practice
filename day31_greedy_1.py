'''贪心算法

局部最优推出整体最优
'''


'''455.分发饼干

'''
class Solution(object): #my sol
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        for i in range(len(g)):
            while s and g[i]>s[0]:
                s=s[1:]
            if not s:
                break
            ans+=1
            s=s[1:]
        return ans

class Solution(object): #遍历饼干 my sol
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        result = 0
        for i in s:
            if g and i >=g[0]:
                g = g[1:]
                result+=1
        return result



class Solution: #标准答案 小饼干优先
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = 0
        for i in range(len(s)):  # 遍历饼干
            if index < len(g) and g[index] <= s[i]:  # 如果当前孩子的贪心因子小于等于当前饼干尺寸
                index += 1  # 满足一个孩子，指向下一个孩子
        return index  # 返回满足的孩子数目

class Solution: #大饼干优先
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = len(s) - 1  # 饼干数组的下标，从最后一个饼干开始
        result = 0  # 满足孩子的数量
        for i in range(len(g)-1, -1, -1):  # 遍历胃口，从最后一个孩子开始
            if index >= 0 and s[index] >= g[i]:  # 遍历饼干
                result += 1
                index -= 1
        return result



'''376. 摆动序列

'''
class Solution(object): # my sol
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        prev = 0
        result = 1
        for i in range(1,len(nums)):
            if prev==0 and nums[i]-nums[i-1]!=0: #峰值
                prev=nums[i]-nums[i-1]
                result+=1
            # elif prev*(nums[i]-nums[i-1])==0:
            #     continue
            elif prev*(nums[i]-nums[i-1])<0: #峰值 可以和前一个if合并
                prev=nums[i]-nums[i-1]
                result+=1
            # else:
            #     # prev+=nums[i]-nums[i-1]
            #     continue #不用真的算数，只是左乘法
        return result



'''53. 最大子序和

'''
class Solution(object): #my sol
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 负数的话就直接重新开始（因为只会让后面的数更小）
        cur_sum = 0
        result = float('-inf')
        for i in nums:
            # if cur_sum==0 and i<=0:
            #     cur_sum+=i
            if cur_sum<0: #无论i是否>0,都重新开始
                cur_sum=i
            else:
                cur_sum+=i
            result=max(cur_sum,result)
        return result

class Solution: #标准答案
    def maxSubArray(self, nums):
        result = float('-inf')  # 初始化结果为负无穷大
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:  # 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count
            if count <= 0:  # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
                count = 0
        return result
