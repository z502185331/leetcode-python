# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        self.sol_stack(head)
    
    
    '''
    One solution by using stack
    '''
    def sol_stack(self, head):
        stack = []
        mid = self.findMid(head)
        
        # cut the list
        tmp = mid.next
        mid.next = None
        mid = tmp
        
        # push all the second half of nodes into stack
        while mid is not None:
            stack.append(mid)
            mid = mid.next
        
        prehead = ListNode(-1)
        prehead.next = head
        while stack:
            tmp = head.next
            head.next = stack.pop()
            head.next.next = tmp
            head = tmp
        return prehead.next
    
    '''
    A method to return the middle node of a list
    @return a middle node
    '''
    def findMid(self, head):
        s, q = head, head.next
        
        while q is not None and q.next is not None:
            s = s.next
            q = q.next.next
        return s