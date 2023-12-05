class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# leetcode 203 移除链表元素

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next

# 注意 ： 设置dummy head， 建立current， 回答dummy head的下一个

# leetcode 707 设计链表

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self,val=0,next=None):
        self.dummy_node = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index <0 or index >= self.size: # need to consider <0 or >= self.size
            return -1
        else:
            # temp = ListNode(next=self.dummy_node)
            # current = temp
            # don't need to go through it again
            current = self.dummy_node.next
            for i in range(index):
                current = current.next
            return current.val

        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.size += 1
        # return ListNode(val=val, next=self.dummy_node)
        # add at head which is right after dummy_node
        self.dummy_node.next = ListNode(val, self.dummy_node.next)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        # temp = ListNode(next=self.dummy_node)
        # current = temp
        # don't need to do this again
        current = self.dummy_node
        for i in range(self.size):
            current = current.next
        current.next=ListNode(val=val)
        self.size += 1

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <0 or index > self.size: # again, please consider < 0
            return
        else:
            # temp = ListNode(next=self.dummy_node)
            # current = temp
            current = self.dummy_node
            for i in range(index):
                current = current.next
            current.next=ListNode(val=val,next=current.next) # 搞清楚啥时候next啥时候next.next
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index >= self.size:
            return
        else:
            # temp = ListNode(next=self.dummy_node)
            # current = temp
            current = self.dummy_node
            for i in range(index):
                current = current.next
            current.next=current.next.next
            self.size -= 1



# leetcode 206 反转链表
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

# 注意改变prev = current， current = temp （把current便成下一个位子）跟下面联系起来

'''（版本二）递归法 '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)