# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        prehead = ListNode(-1)
        prehead.next = head
        
        # count the length of list
        length = 0
        while head is not None:
            head = head.next
            length += 1
        
        k %= length
        
        if k == 0:
            return prehead.next
        
        # find the previous node before the second half
        count = length - k
        node = prehead
        
        while count > 0:
            node = node.next
            count -= 1
        
        first_start = prehead.next
        first_end = node
        
        second_start = node.next
        
        # find the tail node
        while node.next is not None:
            node = node.next
        
        second_end = node
        
        prehead.next = second_start
        second_end.next = first_start
        first_end.next = None
        
        return prehead.next
        
            