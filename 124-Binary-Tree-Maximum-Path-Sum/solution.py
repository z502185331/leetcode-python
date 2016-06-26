# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        localsum, res = self.getMaxSum(root, -sys.maxint - 1)
        return res
        
    
    def getMaxSum(self, root, maxSum):
        if root is None:
            return 0, maxSum
        
        # three conditions:
        # 1. sum(left child) + node.val
        # 2. sum(right child) + node.val
        # 3. sum(left child) + node.val + sum(right child)
        # 4. node.val
        sum_left, max_left = self.getMaxSum(root.left, maxSum)
        sum_right, max_right = self.getMaxSum(root.right, maxSum)
        
        # compare different sum and get max sum
        sum1 = sum_left + root.val
        sum2 = sum_right + root.val
        sum3 = sum_left + root.val + sum_right # this sum will not return to the parent
        
        maxSum = max(sum1, sum2, sum3, root.val, max_left, max_right)
        return max(sum1, sum2, root.val), maxSum