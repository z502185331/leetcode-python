# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # return self.mergeSort(head)
        return self.quickSort(head)
    
    
    def quickSort(self, head):
        if head is None or head.next is None:
            return head
        
        # set a pivot
        pivot = head.val
        prehead1 = ListNode(-1) # prehead for node with value less than pivot
        prehead2 = ListNode(-1) # prehaed for node with value equal to pivot
        prehead3 = ListNode(-1) # prehead for node with value larger than pivot
        tail1, tail2, tail3 = prehead1, prehead2, prehead3
        
        # separate the list by their value
        cur = head
        while cur is not None:
            if cur.val < pivot:
                tail1.next = cur
                tail1 = tail1.next
            elif cur.val == pivot:
                tail2.next = cur
                tail2 = tail2.next
            else:
                tail3.next = cur
                tail3 = tail3.next
            cur = cur.next
        tail1.next, tail2.next, tail3.next = None, None, None
        
        # quick sort the sublist
        prehead1.next = self.quickSort(prehead1.next)
        prehead3.next = self.quickSort(prehead3.next)
        
        # merge the three nodelist
        prehead = ListNode(-1)
        tail = prehead
        tail = self.findTail(tail, prehead1.next)
        tail = self.findTail(tail, prehead2.next)
        tail = self.findTail(tail, prehead3.next)
        
        return prehead.next

    '''
    A method to get the tail of node list
    @return the tail node
    '''
    def findTail(self, tail, head):
        if head is not None:
            tail.next = head
            
        while tail.next is not None:
            tail = tail.next
        return tail
    
    '''
    A method to sort the list by mergesort
    '''
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        
        s, q = head, head.next # find the mid node
        while q is not None and q.next is not None:
            s = s.next
            q = q.next.next
        
        tmp = s.next # cut the list
        s.next = None
        s = tmp
        
        head1 = self.mergeSort(head)
        head2 = self.mergeSort(s)
        prehead = ListNode(-1)
        tail = prehead
        
        # merge two sorted list
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        
        # add left node
        while head1 is not None:
            tail.next = head1
            head1 = head1.next
            tail = tail.next
        while head2 is not None:
            tail.next = head2
            head2 = head2.next
            tail = tail.next
        tail.next = None
        
        return prehead.next