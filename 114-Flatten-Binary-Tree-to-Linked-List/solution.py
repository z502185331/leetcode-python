# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        
        self.helper(root)
    
    
    def helper(self, root):
        if root.left is None and root.right is None:
            return root
        
        left_node, right_node = root.left, root.right
        if root.left is not None:
            left_node = self.helper(root.left)
        
            # Flatten the tree
            root.right = root.left
            left_node.right = right_node
            root.left = None
        
        if right_node is not None:
            right_node = self.helper(right_node)
        else:
            right_node = left_node
        
        return right_node
        
            
        
        