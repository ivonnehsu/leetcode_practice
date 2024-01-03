'''110.平衡二叉树

求高度必须用后序遍历
二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数。 lc104
二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数。 lc110
求深度适合用前序遍历，而求高度适合用后序遍历
the depth of a binary tree is the total number of 
edges from the root node to the most distant leaf node
'''
class Solution: # my sol
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getDepth(root)!= -1
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if left == -1 or right == -1:
            return -1
        if left - right > 1 or left - right < -1: #can use abs()
            return -1
        return 1 + max(left, right)



'''257. 二叉树的所有路径

'''
class Solution: # my sol
    def __init__(self):
        self.output = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.getPath(root,[])
        return self.output
        
    
    def getPath(self, root, route:list):
        route.append(root.val)
        if not root.left and not root.right:
            # print("->".join(str(route)))
            self.output.append("->".join(map(str,route))) #str(i) for i in route
            return
        
        if root.left:
            self.getPath(root.left,route) #可以用route[:] no need to pop then
            route.pop() # this is popping whatever you get from  the previous line 
        if root.right:
            self.getPath(root.right,route)
            route.pop()


class Solution: # 迭代法 把number和path分开

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 题目中节点数至少为1
        stack, path_st, result = [root], [str(root.val)], []

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))

        return result
'''404.左叶子之和

'''
class Solution: # my sol 递归
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return 0
        if not root.left and not root.right: #叶子节点 在父节点的时候才收集
            return 0
        result+=self.sumOfLeftLeaves(root.left)
        if root.left and root.left.left == None and root.left.right == None:
            result+= root.left.val #加号这里 所以不会直接return只有一步份的result
        result+=self.sumOfLeftLeaves(root.right)
        return result

# 精简版
class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        leftValue = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue = root.left.val
        return leftValue + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


# 迭代法
class Solution: # my sol
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        queue = deque([root]) #would be the same idea if using stack []
        result = 0
        while queue:
            cur = queue.popleft()
            if cur.left and not cur.left.left and not cur.left.right:
                result+=cur.left.val
            elif cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result