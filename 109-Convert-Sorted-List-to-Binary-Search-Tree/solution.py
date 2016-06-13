# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if head is None:
            return None
        
        head1, mid, head2 = self.cutList(head)
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head1)
        node.right = self.sortedListToBST(head2)
        return node
        
    
    '''
    A method to cut the list equally
    @return the head node of two lists and its mid node
    '''
    def cutList(self, head):
        if head.next is None:
            return None, head, None
        
        prehead = ListNode(-1)
        prehead.next = head
        s, q = prehead, head.next
        while q is not None and q.next is not None:
            s = s.next
            q = q.next.next
        
        mid = s.next
        s.next = None
        return None if s is prehead else head, mid, mid.next
        
        