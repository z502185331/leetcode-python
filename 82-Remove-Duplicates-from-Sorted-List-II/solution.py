# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        prehead = ListNode(-1)
        prehead.next = head
        
        s, f = prehead, head
        
        while f is not None and f.next is not None:
            if f.val != f.next.val:
                s.next = f
                s = s.next
                f = f.next
            
            else:
                value = f.val
                while f is not None and f.val == value:
                    f = f.next
                
                    
        # deal with last node
        s.next = f
        
        return prehead.next