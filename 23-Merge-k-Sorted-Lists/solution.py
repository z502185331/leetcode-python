# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if not lists:
            return None
            
        heap = []
        for i in xrange(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(heap, (lists[i].val, i))
        
        prehead = ListNode(-1)
        tail = prehead
        while heap:
            num, i = heapq.heappop(heap)
            tail.next = lists[i]
            tail = tail.next
            lists[i] = lists[i].next
            
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
        
        tail.next = None
        return prehead.next
            