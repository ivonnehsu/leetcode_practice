'''stack栈：先进先出，queue：先进后出'''

'''232.用栈实现队列

'''
class MyQueue(object): # my solution

    def __init__(self):
        self.right_stack = [] #stack_in
        self.back_stack = [] #stack_out

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.right_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while self.right_stack:
            self.back_stack.append(self.right_stack.pop())
        temp =  self.back_stack.pop()
        while self.back_stack:
            self.right_stack.append(self.back_stack.pop())
        return temp

    def peek(self):
        """
        :rtype: int
        """
        return self.right_stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.right_stack:
            return True
        else:
            return False


# 标准回复
class MyQueue:

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop()) # stack in pop already remove it from the first list
            return self.stack_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)

'''225. 用队列实现栈

'''

class MyStack(object): # my response

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack


# standard ans
from collections import deque

class MyStack:

    def __init__(self):
        """
        Python普通的Queue或SimpleQueue没有类似于peek的功能
        也无法用索引访问，在实现top的时候较为困难。

        用list可以，但是在使用pop(0)的时候时间复杂度为O(n) ##!!!!!
        因此这里使用双向队列，我们保证只执行popleft()和append()，因为deque可以用索引访问，可以实现和peek相似的功能

        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        """
        直接append即可
        """
        self.queue_in.append(x)


    def pop(self) -> int:
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个
        
        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in    # 交换in和out，这也是为啥in只用来存
        return self.queue_out.popleft()

    def top(self) -> int:
        """
        写法一：
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可（这里实际上用到了栈）
        写法二：
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个，并使用temp变量暂存
        6. 把temp追加到queue_in的末尾
        """
        # 写法一：
        # if self.empty():
        #     return None
        
        # return self.queue_in[-1]    # 这里实际上用到了栈，因为直接获取了queue_in的末尾元素

        # 写法二：
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in 
        temp = self.queue_out.popleft()   
        self.queue_in.append(temp)
        return temp


    def empty(self) -> bool:
        """
        因为只有in存了数据，只要判断in是不是有数即可
        """
        return len(self.queue_in) == 0



'''317 

'''
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(grid), len(grid[0])

        def bfs(candidates,building):
            visited = set()
            distance = 0
            cur = [building]
            while cur:
                distance+=1
                next_level = []
                for position in cur:
                    for direction in directions:
                        next_position = (position[0]+direction[0],position[1]+direction[1])
                        if next_position in candidates and next_position not in visited:
                             candidates[next_position]+=distance
                             visited.add(next_position)
                             next_level.append(next_position)
                cur = next_level
            if len(visited) != len(candidates):
                for position in set(candidates.keys()).difference(visited):
                    candidates.pop(position)



        buildings = []
        candidates = dict()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    buildings.append((i,j))
                if grid[i][j]==0:
                    candidates[(i,j)]=0
        for building in buildings:
            bfs(candidates,building)
        return min(candidates.values()) if buildings and candidates else -1