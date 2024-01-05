'''513.找树左下角的值

'''
class Solution: # my sol 递归法
    def __init__(self):
        self.max_layer = 0 #可以直接把这几个放在后面的function里 #或可出世成-inf
        self.max_val = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.findLeft(root,self.max_layer+1)
        return self.max_val
    def findLeft(self,root,layer):
        if not root.left and not root.right: #终止条件
            if layer>self.max_layer:
                self.max_layer, self.max_val = layer, root.val
        if root.left: #只需优先遍历左
            self.findLeft(root.left,layer+1) #layer+1相当于回溯的过程了
        if root.right:
            self.findLeft(root.right,layer+1)


class Solution: #层序遍历 队列 my sol （这和答案的迭代感觉差不多？）
    # def __init__(self):
    #     self.max_layer = 0
    #     self.max_val = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if _ == 0:
                    val = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return val

'''112. 路径总和

'''
class Solution: #my sol
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        self.valid = False
        if not root:
            return False
        self.getSum(root,root.val)
        return self.valid
        
    def getSum(self,root,val): #不应该算总和 应该做减法
        if not root.left and not root.right and val == self.targetSum: #最终一定会到叶子 所以要么这个要么！=
                self.valid = True
        if root.left:
            self.getSum(root.left,val+root.left.val)
        if root.right:
            self.getSum(root.right,val+root.right.val)

class Solution: #my sol 精简
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSum = targetSum
        if not root:
            return False
        return self.getSum(root,root.val)
        
    def getSum(self,root,val): #不应该算总和 应该做减法
        print(val)
        if not root.left and not root.right and val == self.targetSum:
            print('yes')
            return True
        if not root.left and not root.right:
            return False
        return self.getSum(root.left,val+root.left.val) or self.getSum(root.right,val+root.right.val) # 其一就可以

class Solution: # my sol
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.getSum(root,targetSum - root.val)
        
    def getSum(self,root,val): #减法
        print(val)
        if not root.left and not root.right and val == 0:
            return True
        if not root.left and not root.right:
            return False
        return self.getSum(root.left,val-root.left.val) or self.getSum(root.right,val-root.right.val) #其一就可以

class Solution: #标准
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum ==root.val:
            return True
        if not root.left and not root.right: #这个可以省略
            return False
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)

class Solution: # 迭代
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root,targetSum)]
        while stack:
            cur,val = stack.pop()
            print(cur.val,val)
            if not cur.left and not cur.right and cur.val == val:
                return True
            if cur.left:
                stack.append((cur.left,val-cur.val))
            if cur.right:
                stack.append((cur.right,val-cur.val))
        return False

'''113.路径总和ii

'''
class Solution: # my sol 递归
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = [] #可以直接写result，下面写result
        self.pathRoute(root,targetSum,[])
        return self.result
    def pathRoute(self, node, targetSum, route):
        if not node:
            return
        if not node.left and not node.right and targetSum == node.val:
            self.result.append(route+[node.val])
        elif not node.left and not node.right:
            return
        if node.left:
            self.pathRoute(node.left,targetSum-node.val,route+[node.val])
        if node.right:
            self.pathRoute(node.right,targetSum-node.val,route+[node.val])

# 标准
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        result = []
        self.traversal(root, targetSum, [], result)
        return result
    def traversal(self,node, count, path, result):
            if not node:
                return
            path.append(node.val)
            count -= node.val
            if not node.left and not node.right and count == 0:
                result.append(list(path))
            self.traversal(node.left, count, path, result)
            self.traversal(node.right, count, path, result)
            path.pop()

'''106.从中序与后序遍历序列构造二叉树 

'''
class Solution: # 标准答案 想法有点难 找准中间的点
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return
        root = TreeNode(val=postorder[-1])
        mid_idx = inorder.index(root.val)
        inorder_l = inorder[:mid_idx]
        inorder_r = inorder[mid_idx+1:]
        postorder_l = postorder[:len(inorder_l)]
        postorder_r = postorder[len(inorder_l):len(postorder)-1] #减一因为去掉中间
        root.left= self.buildTree(inorder_l,postorder_l)
        root.right = self.buildTree(inorder_r,postorder_r)
        return root

'''105.从前序与中序遍历序列构造二叉树

'''
class Solution: # mysol
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(val = preorder[0])
        idx = inorder.index(root.val)
        inorder_root_l = inorder[:idx]
        inorder_root_r = inorder[idx+1:]
        preorder_root_r = preorder[idx+1:]
        preorder_root_l = preorder[1:idx+1]
        # 递归
        root.left = self.buildTree(preorder_root_l,inorder_root_l)
        root.right = self.buildTree(preorder_root_r,inorder_root_r)
        return root