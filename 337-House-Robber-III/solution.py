# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        rob_root, no_rob_root = self.rob_helper(root)
        # return max(rob_root, no_rob_root)
        return rob_root
        
    
    def rob_helper(self, root):
        if root is None:
            return 0, 0
        
        rob_left, no_rob_left = self.rob_helper(root.left)
        rob_right, no_rob_right = self.rob_helper(root.right)
        
        rob_self = max(root.val + no_rob_left + no_rob_right, rob_left + rob_right)
        no_rob_self = rob_left + rob_right
        
        return rob_self, no_rob_self