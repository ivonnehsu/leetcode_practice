'''669. 修剪二叉搜索树 

'''
class Solution: # my sol
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        if low <= root.val <= high: #继续遍历
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
        elif root.val < low: #终止条件
            return self.trimBST(root.right,low,high)
        elif root.val > high: #终止条件
            return self.trimBST(root.left,low,high)
        return root

class Solution: #迭代法
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        
        # 处理头结点，让root移动到[L, R] 范围内，注意是左闭右闭
        while root and (root.val < L or root.val > R):
            if root.val < L:
                root = root.right  # 小于L往右走
            else:
                root = root.left  # 大于R往左走
        
        cur = root
        
        # 此时root已经在[L, R] 范围内，处理左孩子元素小于L的情况
        while cur:
            while cur.left and cur.left.val < L:
                cur.left = cur.left.right
            cur = cur.left
        
        cur = root
        
        # 此时root已经在[L, R] 范围内，处理右孩子大于R的情况
        while cur:
            while cur.right and cur.right.val > R:
                cur.right = cur.right.left
            cur = cur.right
        
        return root

'''108.将有序数组转换为二叉搜索树 

'''
class Solution: # my sol
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # if len(nums)==1:
        #     return TreeNode(nums[0])
        mid = len(nums)//2
        # print(len(nums),mid)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

class Solution: #标准
    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid - 1)
        root.right = self.traversal(nums, mid + 1, right)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.traversal(nums, 0, len(nums) - 1)
        return root
        
'''538.把二叉搜索树转换为累加树 

***** 想了 好久 要学会什么时候是赋值 root.right == root.left == 什么时候只是简单的跑一边traverse
不需要返回值 只需要遍历二叉树
'''
class Solution: #my sol
    def __init__(self):
        self.prev = None
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
    def traverse(self,root):
        if not root:
            return
        self.traverse(root.right) #右
        root.val += self.prev if self.prev else 0 #中
        self.prev = root.val
        self.traverse(root.left) #左

class Solution: # 迭代法 标准
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        stack = []
        cur = root
        pre = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else: 
                cur = stack.pop()
                cur.val+= pre
                pre = cur.val
                cur =cur.left
        return root



'''summary

涉及到二叉树的构造，无论普通二叉树还是二叉搜索树一定前序，都是先构造中节点。

求普通二叉树的属性，一般是后序，一般要通过递归函数的返回值做计算。

求二叉搜索树的属性，一定是中序了，要不白瞎了有序性了。

注意在普通二叉树的属性中，我用的是一般为后序，例如单纯求深度就用前序，二叉树：找所有路径 (opens new window)也用了前序，这是为了方便让父节点指向子节点。
'''