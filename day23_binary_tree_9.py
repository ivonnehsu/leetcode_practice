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


'''538.把二叉搜索树转换为累加树 

'''