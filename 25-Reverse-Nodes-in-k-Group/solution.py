# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        prehead = ListNode(-1)
        prehead.next = head
        start = prehead
        
        while self.isEnough(start, k):
            cur = start.next
            for i in xrange(k - 1):
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = start.next
                start.next = tmp
            
            start = cur
        return prehead.next
        
    
    '''
    A method to check whether there are k node in next
    @ return bool 
    '''
    def isEnough(self, node, k):
        
        for i in xrange(k):
            node = node.next
            if node is None:
                return False
        
        return True