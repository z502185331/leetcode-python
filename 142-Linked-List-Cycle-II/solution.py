# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        # find the node in the cycle
        s, q = head, head.next
        while True:
            if q is None or q.next is None: # when the list has no cycle
                return None
                
            if s is q: # find the node
                break
            s = s.next
            q = q.next.next
        
        # calculate the length of cycle
        count = 1
        q = q.next
        while q is not s:
            count += 1
            q = q.next
        
        # let quick point go count step first
        q, s = head, head
        for i in range(count):
            q = q.next
        
        while s is not q:
            s = s.next
            q = q.next
        
        return s