# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
            
        def dfs(root, cur):
            if root is None:
                return False
                
            cur += root.val
            
            if root.left is None and root.right is None:
                return cur == sum
            
            return dfs(root.left, cur) or dfs(root.right, cur)
        
        return dfs(root, 0)