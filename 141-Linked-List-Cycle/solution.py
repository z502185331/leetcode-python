# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False
        
        s, l = head, head.next
        while l is not None and l.next is not None:
            s = s.next
            l = l.next.next
            
            if s is l:
                return True
        
        return False