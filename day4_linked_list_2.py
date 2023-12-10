'''24. 两两交换链表中的节点 
Definition for singly-linked list.

'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(next=head)
        cur = dummyhead
        while cur.next and cur.next.next: # 必须同时满足，如果奇数的话下一个不用换了
            temp = cur.next
            cur.next = cur.next.next
            temp1 = cur.next.next #如果这个定义在上一行之前，防止修改节点，应该变成temp1= cur.next.next.next
            cur.next.next = temp
            cur.next.next.next = temp1 #或可以写成temp.next=temp1, 只需建立联系
            cur = cur.next.next
        return dummyhead.next

# 递归写法
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: #满足其一即可
            return head

        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next # 先同时定义三个
        
        cur.next = pre  # 交换
        pre.next = self.swapPairs(next) # 将以next为head的后续链表两两交换
         
        return cur

'''
19.删除链表的倒数第N个节点 

'''
class Solution(object): # my solution time consuming twisting twice
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def reverseList(head):
          prev = None
          curr = head
          while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
          return prev
        reversed_list = reverseList(head)
        ct = 1
        dummy_head = ListNode(next=reversed_list)
        curr = dummy_head
        while curr:
          if ct == n:
            curr.next = curr.next.next
          else:
            curr = curr.next
          ct+=1
        return reverseList(dummy_head.next)

class Solution(object): # my solution time consuming twisting twice
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # two pointers method
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy_head.next

'''面试题 160 链表相交

'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a, len_b = 0, 0
        current = headA
        while current:
            len_a += 1
            current = current.next
        current = headB
        while current:
            len_b += 1
            current = current.next
        if len_b < len_a:
            len_a,len_b = len_b,len_a
            headA,headB = headB,headA
        diff = len_b - len_a
        curB = headB
        curA = headA
        for _ in range(diff):
            curB = curB.next
        while curB:
            if curB == curA:
                return curB
            else:
                curB = curB.next
                curA = curA.next
        return None

#注意方法 先走，最后的必须会match

###（版本二）求长度，同时出发 （代码复用）
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        # 通过移动较长的链表，使两链表长度相等
        if lenA > lenB:
            headA = self.moveForward(headA, lenA - lenB)
        else:
            headB = self.moveForward(headB, lenB - lenA)
        
        # 将两个头向前移动，直到它们相交
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
    
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def moveForward(self, head: ListNode, steps: int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head

#### 等比例法 如果A+B 和 B+A 相比 最后的重复部分就是重复部分
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA


'''142.环形链表II 

 '''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next: # 注意只用fast and fast.next
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                temp = head
                while fast!=temp: # 注意不等号写在这里 如果while fast 后面写if的话 少涵盖了一个可能性（temp和fast同时开始）
                    temp = temp.next
                    fast = fast.next
                return fast
        return None


### 集合法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None