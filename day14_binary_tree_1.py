'''
理论基础
● 递归遍历  
● 迭代遍历
● 统一迭代
把它理解成一个链表 linked list 类似
'''
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

'''二叉树理论基础'''
# 关于二叉树的遍历方式，要知道二叉树遍历的基本方式都有哪些。

# 一些同学用做了很多二叉树的题目了，可能知道前中后序遍历，可能知道层序遍历，但是却没有框架。

# 我这里把二叉树的几种遍历方式列出来，大家就可以一一串起来了。

# 二叉树主要有两种遍历方式：

# 深度优先遍历：先往深走，遇到叶子节点再往回走。
# 广度优先遍历：一层一层的去遍历。
# 这两种遍历是图论中最基本的两种遍历方式，后面在介绍图论的时候 还会介绍到。

# 那么从深度优先遍历和广度优先遍历进一步拓展，才有如下遍历方式：

# 深度优先遍历
# 前序遍历（递归法，迭代法）
# 中序遍历（递归法，迭代法）
# 后序遍历（递归法，迭代法）
# 广度优先遍历
# 层次遍历（迭代法）
# 在深度优先遍历中：有三个顺序，前中后序遍历， 有同学总分不清这三个顺序，经常搞混，我这里教大家一个技巧。

# 这里前中后，其实指的就是中间节点的遍历顺序，只要大家记住 前中后序指的就是中间节点的位置就可以了。

# 看如下中间节点的顺序，就可以发现，中间节点的顺序就是所谓的遍历方式

# 前序遍历：中左右
# 中序遍历：左中右
# 后序遍历：左右中


'''二叉树递归遍历

底层逻辑： 栈
1. 确认递归函数的参数和返回值
2. 确定终止条件
3. 确定单层递归的逻辑
'''

'''144

前序遍历-递归-LC144_二叉树的前序遍历
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val]+left+right

'''145

'''
class Solution(object): # my solution
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right +[root.val]


'''94

中序遍历
'''
class Solution(object): #my solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left+[root.val]+right

