# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return abs(self.checkBST(root)[0])
    
    
    def checkBST(self, root):
        """
        rtype: int, int, int
        return: the number of nodes, the lower bound, the upper bound
        """
        
        if root is None:
            return 0, sys.maxint, -sys.maxint - 1
        
        left_sum, left_lower, left_upper = self.checkBST(root.left)
        right_sum, right_lower, right_upper = self.checkBST(root.right)
        
        if left_sum < 0 or right_sum < 0 or root.val < left_upper or root.val > right_lower:
            return max(abs(left_sum), abs(right_sum)) * -1, 0, 0
        
        else:
            return left_sum + right_sum + 1, min(left_lower, root.val), max(right_upper, root.val)
        
        