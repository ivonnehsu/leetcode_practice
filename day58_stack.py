'''739. 每日温度

'''
class Solution(object): #brute force - my sol - exceed time limit
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    result[i]=j-i
                    break
        return result

class Solution(object): #using stack
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                temp = stack.pop()
                result[temp] = i - temp
            stack.append(i)
        return result


'''496.下一个更大元素 I 

重新看 不是太清晰
'''
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        ind = nums1.index(nums2[stack[-1]])
                        ans[ind] = nums2[i]
                    stack.pop()
                stack.append(i)
        return ans