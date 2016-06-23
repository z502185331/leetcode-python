# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        prehead_sm, prehead_lg = ListNode(-1), ListNode(-1)
        tail_sm, tail_lg = prehead_sm, prehead_lg
        
        while head is not None:
            if head.val < x:
                tail_sm.next = head
                tail_sm = tail_sm.next
            else:
                tail_lg.next = head
                tail_lg = tail_lg.next
            head = head.next
        
        tail_sm.next = prehead_lg.next
        tail_lg.next = None
        
        return prehead_sm.next