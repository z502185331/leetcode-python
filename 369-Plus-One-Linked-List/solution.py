# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
            
        c = self.sol_recursive(head)
        
        if c != 0:
            node = ListNode(c)
            node.next = head
            head = node
            
        return head
        
    
    def sol_recursive(self, head):
        
        if head is None:
            return 1
        
        c = self.sol_recursive(head.next)
        head.val += c
        c = head.val / 10
        head.val %= 10
        
        return c