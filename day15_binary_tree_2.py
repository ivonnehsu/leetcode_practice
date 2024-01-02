import collections
from collections import deque
'''层序遍历

二叉树的层序遍历 | 广度优先搜索 
10 题'''

#102 binary tree level order traversal
'''队列先进先出，符合一层一层遍历的逻辑，
而用栈先进后出适合模拟深度优先遍历也就是递归的逻辑
而这种层序遍历方式就是图论中的广度优先遍历，只不过我们应用在二叉树上
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
# 递归法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.helper(root, 0, levels)
        return levels
    
    def helper(self, node, level, levels):
        if not node:
            return
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        self.helper(node.left, level + 1, levels)
        self.helper(node.right, level + 1, levels)

# 107  Binary Tree Level Order Traversal II
class Solution(object): # my solution
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)): #长度取于最初
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result[::-1]

# 199.二叉树的右视图
class Solution(object): # my solution
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level[-1])
        return result

class Solution: # 标准答案 只考虑当他是最后一个数的时候 i == level_size-1
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        right_view = []
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                if i == level_size - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view

# 637.二叉树的层平均值
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = 0
            level_len = len(queue)
            for _ in range(level_len):
                cur = queue.popleft()
                level += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            print(level, level_len)
            result.append(round(float(level)/level_len, 5)) # had to switch it to float to pass
        return result

# 429.N叉树的层序遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    for i in node.children:
                        queue.append(i)
            result.append(level)
        return result

# 515.在每个树行中找最大值
class Solution(object): # my solution
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = collections.deque([root])
        largest_values = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            largest_values.append(max(level))
        return largest_values

class Solution: # 标准 每个对比
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            max_val = float('-inf')

            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result


# 116.填充每个节点的下一个右侧节点指针
class Solution(object): # my solution, 赋值prior
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = collections.deque([root])
        result = []
        while queue:
            dummy_head = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if dummy_head:
                    dummy_head.next=cur
                dummy_head = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

# 117.填充每个节点的下一个右侧节点指针II
class Solution(object): # my sol
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = deque([root])
        while queue:
            prior = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if prior:
                    prior.next = cur
                prior = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

# 104.二叉树的最大深度
class Solution(object): # my sol
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([root])
        max_len = 0
        while queue:
            
            for _ in range(len(queue)):
                cur = queue.popleft() # remember this is popleft
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            max_len+=1
        return max_len

# 111.二叉树的最小深度
class Solution(object): # my solution
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([root])
        layer = 0
        while queue:
            layer +=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return layer

'''226 翻转二叉树

'''
class Solution(object): # my solution, 递归前序
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

class Solution(object): # my solution, 迭代遍历，stack栈
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        if not root:
            return root
        stack = [root]
        while stack:
            for _ in range(len(stack)): #有for loop都必须是层序遍历
                node = stack.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root

class Solution(object): # my solution, 迭代遍历，广度优先， queue队列
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        # if not root:
        #     return root
        # stack = [root]
        # while stack:
        #     for _ in range(len(stack)):
        #         node = stack.pop()
        #         node.left, node.right = node.right, node.left
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        # return root
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                node.left,node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
'''101 对称二叉树

'''

class Solution(object): #递归
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.comparison(root.left, root.right)
    
    def comparison(self,right,left):
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif  left == None and right == None:
            return True
        elif left.val != right.val:
            return False
        
        outsider = self.comparison(right.right, left.left)
        insider = self.comparison(left.right,right.left)
        return outsider and insider

test = Solution()
print(test.isSymmetric([1,2,2,3,4,4,3]))

# 迭代法 队列
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

# 迭代法 栈
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        stack.append(root.right)
        stack.append(root.left)
        while stack:
            left = stack.pop()
            right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append(right.right)
            stack.append(left.left)
            stack.append(right.left)
            stack.append(left.right)
        return True

# 层次遍历
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = collections.deque([root.left,root.right])
        while queue:
            level_len = len(queue)

            if level_len%2 !=0: #直接排除如果数量不等
                return False
            level_val = []
            for _ in range(level_len):
                cur = queue.popleft()
                if cur:
                    level_val.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level_val.append(None)
            if level_val != level_val[::-1]: return False
        return True