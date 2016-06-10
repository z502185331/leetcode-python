# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        odd_head = ListNode(-1)
        even_head = ListNode(-1)
        odd_tail, even_tail = odd_head, even_head
        
        i = 1
        while head is not None:
            if (i & 1) == 1:
                odd_tail.next = head
                odd_tail = odd_tail.next
            else:
                even_tail.next = head
                even_tail = even_tail.next
            i += 1
            head = head.next
        
        odd_tail.next = even_head.next
        even_tail.next = None
        return odd_head.next
        