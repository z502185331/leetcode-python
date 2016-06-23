# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        prehead = ListNode(head.val)
        
        while head is not None:
            next_node = head.next
            
            # First node
            if prehead.next is None:
                prehead.next = head
                head.next = None
            
            else:
                tmp = prehead
                while tmp.next is not None:
                    if head.val <= tmp.next.val:
                        head.next = tmp.next
                        tmp.next = head
                        break
                    tmp = tmp.next
                
                # the head.val is larger than the last one
                if tmp.next is None:
                    tmp.next = head
                    head.next = None
            
            head = next_node
        
        return prehead.next