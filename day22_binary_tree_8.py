'''235. 二叉搜索树的最近公共祖先

跟前一天236比起来简单一点 因为是搜索树
二叉搜索树不用讲究顺序
'''
class Solution: # my sol. comment outs are using the method for 236 递归
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root == p or root == q or not root:
        #     return root
        # left = self.lowestCommonAncestor(root.left,p,q)
        # right = self.lowestCommonAncestor(root.right,p,q)
        # if left and right:
        #     return root
        # elif left: return left
        # else: return right
        if not root or p.val == root.val or q.val == root.val:  #1
            return root
        if p.val < root.val < q.val or q.val < root.val < p.val: #1 
            return root
        elif p.val < root.val and q.val < root.val: return self.lowestCommonAncestor(root.left,p,q)
        else: return self.lowestCommonAncestor(root.right,p,q) # 2 
        # 可以调换 1 和2的顺序，可以省略直接return root， else: return root) 类似于迭代的逻辑

class Solution: # my sol. 迭代
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## 迭代
        cur = root
        while cur: #不用用cur去替代root 可以直接while root
            if q.val < cur.val and p.val < cur.val:
                cur = cur.left
            elif q.val > cur.val and p.val > cur.val:
                cur = cur.right
            # elif q.val<cur.val<p.val or p.val<cur.val<q.val:
            #     return cur
            else:
                return cur
        # 保险起见可以加这个
        return None

'''701.二叉搜索树中的插入操作

永远都可以在叶子结点上面插入
'''
class Solution: #why does pre not matter 相当于前序，下移的时候已经确保了满足pre的条件了 my sol 所以只用考虑单层就可以了
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        # pre = None
        cur = root
        self.insertBST(cur,val)
        return root
    def insertBST(self,cur,val):
        if cur.right and cur.val<val:
            # pre=cur.val
            self.insertBST(cur.right,val)
        if cur.left and cur.val>val:
            # pre=cur.val
            self.insertBST(cur.left,val)
        if cur.val<val and not cur.right:
            cur.right = TreeNode(val)
        if val<cur.val and not cur.left:
            cur.left = TreeNode(val)
        # if not cur.right and cur.val<val:
        #     cur.right=TreeNode(val)
        #     return
        # if not cur.left and cur.val>val:
        #     cur.left=TreeNode(val)
        #     return
        # if (pre<cur.val<val or cur.val<val<pre) and not cur.right:
        #     cur.right = TreeNode(val)
        #     return 
        # elif (pre<val<cur.val or val<cur.val<pre) and not cur.left:
        #     cur.left = TreeNode(val)
        #     return

class Solution: #标准
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return TreeNode(val)
        elif root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root

class Solution: #标准 简洁
    def insertIntoBST(self, root, val):
        if root is None:
            node = TreeNode(val)
            return node

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root

class Solution: #迭代 相当于记录一下pre/parent 一直赋值去parent 直到没有cur 直接赋值parent的child
    def insertIntoBST(self, root, val):
        if root is None:  # 如果根节点为空，创建新节点作为根节点并返回
            node = TreeNode(val)
            return node

        cur = root
        parent = root  # 记录上一个节点，用于连接新节点
        while cur is not None:
            parent = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right

        node = TreeNode(val)
        if val < parent.val:
            parent.left = node  # 将新节点连接到父节点的左子树
        else:
            parent.right = node  # 将新节点连接到父节点的右子树

        return root


'''450.删除二叉搜索树中的节点 

涉及到改树的结构
'''
class Solution: # my sol
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else: # key == root.val #终止条件
            if not root.left: #单孩子or叶子
                return root.right
            if not root.right: #单孩子or叶子
                return root.left
            else: #是中间的结点 有左右孩子 统一把右孩子扯过来
                cur = root.right
                temp = cur #也可以不用cur 最后返回的时候返回root.right
                while temp.left:
                    temp = temp.left
                temp.left=root.left
                return cur
        return root