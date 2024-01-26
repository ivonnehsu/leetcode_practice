'''435. 无重叠区间

'''
class Solution(object): # my sol 思路不太对 不应该用prev 应该直接改数字
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)<=1: return 0
        intervals.sort(key=lambda x: (x[0],x[1]))
        prev = intervals[0]
        removal = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[i][1]<prev[1]:
                removal+=1
                prev = intervals[i]
            elif intervals[i][0]<prev[1]:
                removal+=1
            else:
                prev = intervals[i]
        return removal

class Solution: #标准答案 
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])  # 按照左边界升序排序
        count = 0  # 记录重叠区间数量
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:  # 存在重叠区间
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])  # 更新重叠区间的右边界
                count += 1
        
        return count

'''763.划分字母区间

'''
class Solution(object): #my sol
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=[i]
            else:
                dic[s[i]].append(i)
        dic = dic.values()
        dic.sort(key=(lambda x: x[0]))
        result = []
        for i in range(1,len(dic)):
            if dic[i][0]<dic[i-1][-1]:
                dic[i][-1]=max(dic[i-1][-1],dic[i][-1])
                print(dic[i])
            else:
                result.append(dic[i-1][-1]+1-sum(result))
        result.append(len(s)-sum(result))
        return result

class Solution: #答案
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}  # 存储每个字符最后出现的位置
        for i, ch in enumerate(s):
            last_occurrence[ch] = i

        result = []
        start = 0
        end = 0
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])  # 找到当前字符出现的最远位置
            if i == end:  # 如果当前位置是最远位置，表示可以分割出一个区间
                result.append(end - start + 1)
                start = i + 1

        return result
        
'''56. 合并区间

'''
class Solution(object): #my sol
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        if len(intervals)<=1: return intervals
        result = []
        for i in range(1,len(intervals)):
            if intervals[i][0]<=intervals[i-1][1]:
                intervals[i]=[intervals[i-1][0], #递增，所以这个肯定是最小的
                max(intervals[i][1],intervals[i-1][1])]
            else:result.append(intervals[i-1])
        result.append(intervals[-1])
        return result

class Solution: #标准答案 直接放一个在result数组里面 不用重复添加
    def merge(self, intervals):
        result = []
        if len(intervals) == 0:
            return result  # 区间集合为空直接返回

        intervals.sort(key=lambda x: x[0])  # 按照区间的左边界进行排序

        result.append(intervals[0])  # 第一个区间可以直接放入结果集中

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:  # 发现重叠区间
                # 合并区间，只需要更新结果集最后一个区间的右边界，因为根据排序，左边界已经是最小的
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])  # 区间不重叠

        return result
