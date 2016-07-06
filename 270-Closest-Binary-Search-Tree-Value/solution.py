# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        if root is None:
            return 0
        
        return self.binarySearch(root, target, None)
        
        
        
    def binarySearch(self, node, target, closestVal):
        if node is None:
            return closestVal
        
        # update the closestVal
        if closestVal is None or abs(node.val - target) < abs(closestVal - target):
            closestVal = node.val
            
        if target > node.val:
            return self.binarySearch(node.right, target, closestVal)
        elif target < node.val:
            return self.binarySearch(node.left, target, closestVal)
        else:
            return node.val
        
        