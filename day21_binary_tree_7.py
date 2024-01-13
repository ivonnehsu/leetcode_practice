'''530.二叉搜索树的最小绝对差

采用中序遍历
'''
class Solution: #my code 递归法（版本一）利用中序递增，结合数组
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return
        self.ordered_nums = []
        # print(self.ordered_nums)
        minimum_num = float('inf')
        self.orderNums(root)
        if len(self.ordered_nums)==2:
            return abs(self.ordered_nums[1]-self.ordered_nums[0])
        for i in range(1,len(self.ordered_nums)):
            # 可以直接用min？
            if minimum_num > self.ordered_nums[i]-self.ordered_nums[i-1]:
                minimum_num = self.ordered_nums[i]-self.ordered_nums[i-1]
        return minimum_num
    
    def orderNums(self,root):
        # if root.left:
        #     self.orderNums(root.left)
        # self.ordered_nums.append(root.val)
        # if root.right:
        #     self.orderNums(root.right)
        if root is None:
            return
        self.traversal(root.left)
        self.vec.append(root.val)  # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

class Solution: # clean 递归法（版本一）利用中序递增，结合数组
    def __init__(self):
        self.vec = []

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.vec.append(root.val)  # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

    def getMinimumDifference(self, root):
        self.vec = []
        self.traversal(root)
        if len(self.vec) < 2:
            return 0
        result = float('inf')
        for i in range(1, len(self.vec)):
            # 统计有序数组的最小差值
            result = min(result, self.vec[i] - self.vec[i - 1])
        return result

class Solution: # 递归法（版本二）利用中序递增，找到该树最小值。两个指针
    def __init__(self):
        self.result = float('inf')
        self.pre = None

    def traversal(self, cur):
        if cur is None:
            return
        self.traversal(cur.left)  # 左
        if self.pre is not None:  # 中
            self.result = min(self.result, cur.val - self.pre.val)
        self.pre = cur  # 记录前一个
        self.traversal(cur.right)  # 右

    def getMinimumDifference(self, root):
        self.traversal(root)
        return self.result

class Solution: #迭代
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev = None
        cur = root
        result = float('inf')
        while cur or len(stack)>0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev is not None:
                    result = min(cur.val-prev, result)
                prev = cur.val
                cur = cur.right #需要加上这一步！
        return result

'''501.二叉搜索树中的众数

可以采用defaultdict
'''
class Solution: #my sol, kinda 双指针
    def __init__(self):
        self.result = None
        self.prev_ct = [None,None]
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #中序遍历？
        self.traverse(root)
        return self.result[0]

    def traverse(self,cur):
        if not cur:
            return
        self.traverse(cur.left)
        if self.prev_ct and self.prev_ct[0]==cur.val:
            self.prev_ct[1]+=1
        else:
            self.prev_ct = [cur.val,1]
        if not self.result:
            self.result = [[cur.val],1]
        elif self.result[1]<self.prev_ct[1]:
            self.result = [[self.prev_ct[0]],self.prev_ct[1]]
        elif self.result[1]==self.prev_ct[1]:
            self.result[0]+=[cur.val]
        self.traverse(cur.right)
        

class Solution: #标准答案 递归 利用二叉搜索树性质
    def __init__(self):
        self.maxCount = 0  # 最大频率
        self.count = 0  # 统计频率
        self.pre = None
        self.result = [] #这样分4个比较符合常理 理解 

    def searchBST(self, cur):
        if cur is None:
            return

        self.searchBST(cur.left)  # 左
        # 中
        if self.pre is None:  # 第一个节点
            self.count = 1
        elif self.pre.val == cur.val:  # 与前一个节点数值相同
            self.count += 1
        else:  # 与前一个节点数值不同
            self.count = 1
        self.pre = cur  # 更新上一个节点

        if self.count == self.maxCount:  # 如果与最大值频率相同，放进result中
            self.result.append(cur.val)

        if self.count > self.maxCount:  # 如果计数大于最大值频率
            self.maxCount = self.count  # 更新最大频率
            self.result = [cur.val]  # 很关键的一步，不要忘记清空result，之前result里的元素都失效了

        self.searchBST(cur.right)  # 右
        return

    def findMode(self, root):
        self.count = 0
        self.maxCount = 0
        self.pre = None  # 记录前一个节点
        self.result = []

        self.searchBST(root)
        return self.result

class Solution: #迭代
    def findMode(self, root):
        st = []
        cur = root
        pre = None
        maxCount = 0  # 最大频率
        count = 0  # 统计频率
        result = []

        while cur is not None or st:
            if cur is not None:  # 指针来访问节点，访问到最底层
                st.append(cur)  # 将访问的节点放进栈
                cur = cur.left  # 左
            else:
                cur = st.pop()
                if pre is None:  # 第一个节点
                    count = 1
                elif pre.val == cur.val:  # 与前一个节点数值相同
                    count += 1
                else:  # 与前一个节点数值不同
                    count = 1

                if count == maxCount:  # 如果和最大值相同，放进result中
                    result.append(cur.val)

                if count > maxCount:  # 如果计数大于最大值频率
                    maxCount = count  # 更新最大频率
                    result = [cur.val]  # 很关键的一步，不要忘记清空result，之前result里的元素都失效了

                pre = cur
                cur = cur.right  # 右

        return result

'''236. 二叉树的最近公共祖先

'''
class Solution: #参考答案写出的大幅 要考虑到所有情况 以及什么时候直接返回
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 后序遍历？
        # print('p',p)
        left = None
        right = None
        if root==p or root==q or not root:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        # print(root.val,root.left.val)
        right = self.lowestCommonAncestor(root.right,p,q)
        # print(root.val,root.left.val)
        if left and right:
            return root
        # 以下情况都没考虑到
        if not left and right:
            return right #如果都集中在右边 那就是右边
        elif not right and left:
            return left
        else:
            return None

class Solution: #精简 标准答案
    def lowestCommonAncestor(self, root, p, q):
        if root == q or root == p or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None:
            return right
        return left