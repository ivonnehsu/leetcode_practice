from typing import List

'''栈/stack: []
queue/队列: deque()'''

'''20.有效的括号

栈的经典应用
'''
# temp = []
# print(temp.pop())

class Solution: # my solution
    def isValid(self, s: str) -> bool:
        remaining=[]
        for i in s:
            if i =='(':
                remaining.append(')')
            elif i =='[':
                remaining.append(']')
            elif i =='{':
                remaining.append('}')
            else: #最后的逻辑可以改写成 elif not remaining or remaining[-1]!=i
                try:
                    right = remaining.pop()
                except:
                    return False
                if right != i:
                    return False
        return not remaining

# 栈
# 方法一，仅使用栈，更省空间
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        
        return True if not stack else False

# 方法二，使用字典
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys(): #其实相当于简写了很多if statement
                stack.append(mapping[item])
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        return True if not stack else False # return not stack

'''1047. 删除字符串中的所有相邻重复项

要知道栈为什么适合做这种类似于爱消除的操作，因为栈帮助我们记录了 遍历数组当前元素时候，前一个元素是什么。
'''
class Solution: # my solution with stack
    def removeDuplicates(self, s: str) -> str:
        remaining = [s[0]]
        for i in s[1:]:
            if remaining and i == remaining[-1]:
                remaining.pop()
            else:
                remaining.append(i)
        return ''.join(remaining)


# 方法二，使用双指针模拟栈，如果不让用栈可以作为备选方法。
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
            
        return ''.join(res[0: slow])


'''150. 逆波兰表达式求值

'''
class Solution: # my solution
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))#直接变int
            else:
                num = int(stack.pop())
                if i == '+':
                    stack.append(stack.pop()+num)
                if i == '-':
                    stack.append(stack.pop()-num)
                if i == '*':
                    stack.append(stack.pop()*num)
                if i == '/':
                    stack.append(int(stack.pop()/num))
                    # eval(f'{first_num} {operator} {second_num}')
        return int(stack[0])
        
temp = Solution()
print(int(6/(-132)))

# 用operator
from operator import add, sub, mul

class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面
        return stack.pop()


# 用eval，就是比较慢
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                first_num, second_num = stack.pop(), stack.pop()
                stack.append(
                    int(eval(f'{second_num} {item} {first_num}'))   # 第一个出来的在运算符后面
                )
        return int(stack.pop()) # 如果一开始只有一个数，那么会是字符串形式的