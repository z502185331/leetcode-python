# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        prehead = ListNode(-1)
        prehead.next = head
        
        # find the m - 1 node
        start_node = prehead
        for i in xrange(m - 1):
            start_node = start_node.next
        
        # reverse
        cur = start_node.next
        for i in xrange(n - m):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = start_node.next
            start_node.next = tmp
        
        return prehead.next
        