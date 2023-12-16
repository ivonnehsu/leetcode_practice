from typing import List
'''28. 实现 strStr() 

'''
class Solution(object): #my solution 这个方法会重复每一次 比较绕
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1


####Next方法 只关于模式串
# 字符串的前缀是指不包含最后一个字符的所有以第一个字符开头的连续子串；
# 后缀是指不包含第一个字符的所有以最后一个字符结尾的连续子串
# O(m+n) instead of O(m*n)
# haystack 文本串 needle模式串
# 初始化： 定义两个指针i和j，j指向前缀末尾位置，i指向后缀末尾位置
# 处理前后缀不相同的情况： 因为j初始化为-1，那么i就从1开始，进行s[i] 与 s[j+1]的比较。如不同，找 j+1前一个元素在next数组里的值（就是next[j]） WHILE
# 处理前后缀相同的情况： 如果 s[i] 与 s[j + 1] 相同，那么就同时向后移动i 和j 说明找到了相同的前后缀，同时还要将j（前缀的长度）赋给next[i], 因为next[i]要记录相同前后缀的长度
class Solution:
    def getNext(self, next: List[int], s: str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1
        
'''459.重复的子字符串
 
'''

