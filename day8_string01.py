from typing import List
'''344.反转字符串 
# 双指针，原地操作
'''
# 直接用reversed
class Solution: #kinda my solution
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = reversed(s)

#双指针,两个指针都变动的
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(len(s)//2)更低
        # 因为while每次循环需要进行条件判断，而range函数不需要，直接生成数字，因此时间复杂度更低。推荐使用range
        while left < right:
            s[left], s[right] = s[right], s[left] #可以直接变换
            left += 1
            right -= 1

#栈
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for char in s:
            stack.append(char)
        for i in range(len(s)):
            s[i] = stack.pop()

#range
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
       

#切片
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
       
#reverse（）
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 原地反转,无返回值
        s.reverse() #方式和sort差不多。sort(): inplace, sorted(): new one

#列表推倒
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = [s[i] for i in range(len(s) - 1, -1, -1)]
       
'''541. 反转字符串II 

'''
class Solution: #my solution
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        s_lst = list(s)
        while i < len(s_lst):
            if i+k < len(s_lst):
                s_lst[i:i+k]=reversed(s_lst[i:i+k]) # reverse() can only do list in general, reversed() can do towards anything that's iterable
            else:
                s_lst[i:]=reversed(s_lst[i:])
            i+=2*k
        return ''.join(s_lst)
# temp = Solution()
# print(temp.reverseStr("abcdefg",2))

# 另一写法
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s

#用two pointer
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        
        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])
        
        return ''.join(res)

'''54.替换数字 kamacoder

给定一个字符串 s，它包含小写字母和数字字符，
请编写一个函数，将字符串中的字母字符保持不变，
而将每个数字字符替换为number

例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。

对于输入字符串 "a5b"，函数应该将其转换为 "anumberb"

输入：一个字符串 s,s 仅包含小写字母和数字字符。

输出：打印一个新的字符串，其中每个数字字符都被替换为了number
'''
class Solution: #my solution? -> this would not work because the size change
    # should consider changing from the back 从后向前填充
    def replace_number(self,s:str) -> str:
        if s[-1].isnumeric():
            s = s[:-1]+'number'
        for i in range(len(s)-2,-1,-1):
            if s[i].isnumeric():
                s = s[:i]+'number'+s[i+1:]
        return s
test= Solution()
print(test.replace_number('a5b'))
print(test.replace_number('a1b2c3'))

'''151.翻转字符串里的单词
## 不要使用辅助空间，空间复杂度要求为O(1)。

## 所以解题思路如下：
移除多余空格
将整个字符串反转
将每个单词反转

'''
class Solution: #my solution
    def reverseWords(self, s: str) -> str:
        s_lst = s.split(' ')
        # print(s_lst)
        n_lst = []
        for i in range(len(s_lst)-1,-1,-1):
            if s_lst[i] != '':
                n_lst.append(s_lst[i])
        return ' '.join(n_lst)

# 答案版本1
class Solution:
    def reverseWords(self, s: str) -> str:
        # 删除前后空白
        # s = s.strip()
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并反转每个单词 #字符串是不可变类型
        s = ' '.join(word[::-1] for word in s.split())
        return s

s = " a good   example"
print('1, ', s.split()) # split 会直接split所有空格！
print('2, ', s.split(' '))
temp = Solution()
print(temp.reverseWords(" a good   example"))

# 版本2 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()
        print(words)

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)
temp = Solution()
print(temp.reverseWords(" a good   example"))


'''18. 55.右旋转字符串 kamacoder

'''
class Solution:
    def right_rotate_string(self, k:int, s:str)->str:
        l = len(s)
        s = s[-k:]+s[:l-k]
        return s
temp = Solution()
print(temp.right_rotate_string(2,"abcdefg"))