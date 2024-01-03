'''104.二叉树的最大深度

求高度：后序遍历 递归 找到孩子之后层层+1
求深度：前序遍历 递归 中左右
'''
class Solution(object): # my sol 后序遍历，递归  快
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)

    def getDepth(self, root):
        if not root:
            return 0
        else: # else 这部分可以省略
            left_node = self.getDepth(root.left) #左
            right_node = self.getDepth(root.right) #右
            max_cur_node = 1 + max(left_node, right_node) #中
        return max_cur_node

#精简版本 最快
class solution:
    def maxdepth(self, root: treenode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))

#层次迭代 慢
class Solution(object): # my sol
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth

'''559.n叉树的最大深度

'''
#递归法
class Solution(object): 
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        max_depth = 1
        for i in root.children:
             max_depth = max(max_depth,1+self.maxDepth(i))
        return max_depth

# 迭代遍历 队列 
class Solution(object): 
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([root])
        max_depth = 0
        while queue:
            max_depth+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children: # 必须单个单个append
                    queue.append(child)
        return max_depth
'''111.二叉树的最小深度

'''
# my sol, 递归法
class Solution(object): #left node needs to be with no children at all
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: # no val/root.left/root.right
            return 0
        if root.left==None and root.right != None: # no root.left
            return 1 + self.minDepth(root.right)
        if root.right==None and root.left != None: # no root.right
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))


# 递归
class Solution:
    def getDepth(self, node):
        if node is None:
            return 0
        leftDepth = self.getDepth(node.left)  # 左
        rightDepth = self.getDepth(node.right)  # 右
        
        # 当一个左子树为空，右不为空，这时并不是最低点
        if node.left is None and node.right is not None:
            return 1 + rightDepth
        
        # 当一个右子树为空，左不为空，这时并不是最低点
        if node.left is not None and node.right is None:
            return 1 + leftDepth
        
        result = 1 + min(leftDepth, rightDepth) #中
        return result

    def minDepth(self, root):
        return self.getDepth(root)

'''222.完全二叉树的节点个数

'''
# 递归 O(n)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        cur = 1 + left + right
        return cur

# 完全二叉树写法
class Solution: # my sol
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ## 二叉树
        # if not root:
        #     return 0
        # left = self.countNodes(root.left)
        # right = self.countNodes(root.right)
        # cur = 1 + left + right
        # return cur

        ## 完全二叉树
        if not root:
            return 0
        left = root.left
        right = root.right
        left_len = 1
        right_len = 1
        while left:
            left_len += 1
            left = left.left
        while right:
            right_len += 1
            right = right.right
        if left_len == right_len:
            return 2**left_len - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution: #简化
    def countNodes(self, root: Optional[TreeNode]) -> int: 

        ## 完全二叉树
        if not root:
            return 0
        left = root.left
        right = root.right
        leng = 1
        while left and right:
            leng += 1
            left = left.left
            right = right.right
        if not left and not right:
            return 2**leng - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

