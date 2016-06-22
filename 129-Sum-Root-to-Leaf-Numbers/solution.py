# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = self.helper(root, 0)
        return sum(res)
    
    
    def helper(self, root, cur):
        if root is None:
            return []
            
        cur = cur * 10 + root.val
        
        if root.left is None and root.right is None:
            return [cur]
        
        res = []
        res += self.helper(root.left, cur)
        res += self.helper(root.right, cur)
        
        return res