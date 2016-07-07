# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
    
        heap = []
        res = []
        self.binarySearch(root, target, k, heap)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
    
    def binarySearch(self, node, target, k, heap):
        if node is None:
            return
        
        # update the closestVal
        cur_diff = abs(node.val - target)
        if len(heap) < k:
            heapq.heappush(heap, (-cur_diff, node.val))
        else:
            peak_diff = -heap[0][0]
            if cur_diff < peak_diff:
                heapq.heappop(heap)
                heapq.heappush(heap, (-cur_diff, node.val))
            
        # if target > node.val:
        self.binarySearch(node.right, target, k, heap)
        # elif target < node.val:
        self.binarySearch(node.left, target, k, heap)
        