'''654.最大二叉树 

构造二叉树，都是用中前后（前序遍历）
'''
class Solution: #my sol， 切片
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid_idx=nums.index(max(nums))
        node = TreeNode(val=nums[mid_idx])
        mid_l = nums[:mid_idx]
        mid_r = nums[mid_idx+1:]
        node.left = self.constructMaximumBinaryTree(mid_l)
        node.right = self.constructMaximumBinaryTree(mid_r)
        return node

class Solution: #使用下标 方法
    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left >= right: #必须要确认大小
            return None
        maxValueIndex = left
        for i in range(left + 1, right):
            if nums[i] > nums[maxValueIndex]:
                maxValueIndex = i
        root = TreeNode(nums[maxValueIndex])
        root.left = self.traversal(nums, left, maxValueIndex)
        root.right = self.traversal(nums, maxValueIndex + 1, right)
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.traversal(nums, 0, len(nums))

'''617.合并二叉树 

'''
class Solution: #应该直接在tree1上面改 my sol
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        elif not root1:
            new_root = TreeNode(root2.val)
            new_root.left = self.mergeTrees(root1=None, root2=root2.left)
            new_root.right = self.mergeTrees(root1=None, root2=root2.right)
        elif not root2:
            new_root = TreeNode(root1.val)
            print(new_root)
            new_root.left=self.mergeTrees(root1=root1.left,root2=None)
            new_root.right = self.mergeTrees(root1=root1.right,root2=None)
        else:
            new_root = TreeNode(val=root1.val+root2.val)
            new_root.left = self.mergeTrees(root1.left,root2.left)
            new_root.right = self.mergeTrees(root1.right,root2.right)
        return new_root

class Solution: # 标准
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 递归终止条件: 
        #  但凡有一个节点为空, 就立刻返回另外一个. 如果另外一个也为None就直接返回None. 
        if not root1: 
            return root2
        if not root2: 
            return root1
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空. 
        root1.val += root2.val # 中
        root1.left = self.mergeTrees(root1.left, root2.left) #左
        root1.right = self.mergeTrees(root1.right, root2.right) # 右
        
        return root1 # ⚠️ 注意: 本题我们重复使用了题目给出的节点而不是创建新节点. 节省时间, 空间. 

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 递归终止条件: 
        #  但凡有一个节点为空, 就立刻返回另外一个. 如果另外一个也为None就直接返回None. 
        if not root1: 
            return root2
        if not root2: 
            return root1
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空. 
        root = TreeNode() # 创建新节点
        root.val += root1.val + root2.val# 中
        root.left = self.mergeTrees(root1.left, root2.left) #左
        root.right = self.mergeTrees(root1.right, root2.right) # 右
        
        return root # ⚠️ 注意: 本题我们创建了新节点. 

class Solution: #迭代
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque()
        queue.append((root1, root2))

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right

        return root1      
'''700.二叉搜索树中的搜索 

'''
class Solution: # my sol
    #binary search tree (BST)
    #左边一定小于中间小于右边
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)

class Solution: # 迭代
    #binary search tree (BST)
    #左边一定小于中间小于右边
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
        return

'''98.验证二叉搜索树 


'''
class Solution: #my sol 需要创建数组
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.number_lst = []
        self.cumulateNumber(root)
        for i in range(1,len(self.number_lst)):
            if self.number_lst[i-1]>=self.number_lst[i]:
                return False
        return True

        
    def cumulateNumber(self,root):
        if not root:
            return
        if root.left:
            self.cumulateNumber(root.left)
        self.number_lst.append(root.val)
        if root.right:
            self.cumulateNumber(root.right)
        
class Solution: #递归，极小值比较
    def __init__(self):
        self.maxVal = float('-inf')  # 因为后台测试数据中有int最小值

    def isValidBST(self, root):
        if root is None:
            return True

        left = self.isValidBST(root.left)
        # 中序遍历，验证遍历的元素是不是从小到大
        if self.maxVal < root.val:
            self.maxVal = root.val
        else:
            return False
        right = self.isValidBST(root.right)

        return left and right

class Solution: #递归 直接取最小值
    def __init__(self):
        self.pre = None  # 用来记录前一个节点

    def isValidBST(self, root):
        if root is None:
            return True

        left = self.isValidBST(root.left)

        if self.pre is not None and self.pre.val >= root.val:
            return False
        self.pre = root  # 记录前一个节点

        right = self.isValidBST(root.right)
        return left and right

class Solution: #迭代
    def isValidBST(self, root):
        stack = []
        cur = root
        pre = None  # 记录前一个节点
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left  # 左
            else:
                cur = stack.pop()  # 中
                if pre is not None and cur.val <= pre.val:
                    return False
                pre = cur  # 保存前一个访问的结点
                cur = cur.right  # 右
        return True
